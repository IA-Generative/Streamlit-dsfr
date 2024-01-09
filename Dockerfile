#syntax=docker/dockerfile:1.4

# This Dockerfile uses the root folder as context.


# --
# Upstream images

FROM python:3.10-slim AS python_upstream
FROM node:20-slim AS node_upstream


# --
# Npm image

FROM node_upstream AS npm

# Create app directory
WORKDIR /app

# Source code should be mounted here
VOLUME /app

COPY --link --chmod=755 ./frontend/docker-npm-entrypoint.sh /usr/local/bin/docker-npm-entrypoint

ENTRYPOINT [ "docker-npm-entrypoint" ]
CMD [ "--help" ]


# --
# Node Base image

FROM node_upstream AS app_node_base

# Create app directory
WORKDIR /app

# Set exposed port
ARG PORT=80
ENV PORT=${PORT}

# Install dev dependencies, required in dev & build
COPY --link ./frontend/app/package*.json ./frontend/app/tsconfig*.json ./frontend/app/*.config.* .
RUN npm clean-install --include=dev && \
	npm cache clean --force


# --
# Node Dev image

FROM app_node_base AS app_node_dev

ENV APP_ENV=dev
ENV NODE_ENV=development

# Source code should be mounted here
VOLUME /app
VOLUME /app/node_modules

# Expose port
EXPOSE ${PORT}

COPY --link --chmod=755 ./frontend/docker-dev-command.sh /usr/local/bin/docker-dev-command

CMD [ "docker-dev-command" ]


# --
# Node Prod build image

FROM app_node_base AS app_node_prod_build

ENV APP_ENV=prod
ENV NODE_ENV=production

# Copy source code
COPY --link ./frontend/app .

# Create symlink to streamlit component library
# Workaround for "Unexpected token 'export'" error
RUN ln -s /app/node_modules/streamlit-component-lib/dist ./src/stcomponentlib

# Build application
RUN npm run build


# --
# Node Prod image

FROM nginx_upstream AS app_node_prod

ENV APP_ENV=prod
ENV NODE_ENV=production

# Set app directory
WORKDIR /usr/share/nginx/html

# Copy built static website files
COPY --from=app_node_prod_build --link /app/dist .


# --
# Python Base image

FROM python_upstream AS app_python_base

# Create app directory
WORKDIR /app

# Set exposed port
ARG PORT=80
ENV PORT=${PORT}


# --
# Python Dev image

FROM app_python_base AS app_python_dev

ENV APP_ENV=dev
ENV PYTHONPATH=.

# Install as editable package
COPY --link ./app/app .
RUN pip install --no-cache-dir -e .

# Source code should be mounted here
VOLUME /app
VOLUME /app/demo

# Expose port
EXPOSE ${PORT}

CMD [ "sh", "-c", "streamlit run demo/app.py --server.port ${PORT}" ]


# --
# Python Prod build image

FROM app_python_base AS app_python_prod_build

ENV APP_ENV=prod

# Copy source code
COPY --link ./app/app .

# Set release flag to true
RUN sed -i 's/^_RELEASE = False/_RELEASE = True/g' ./streamlit_dsfr/__init__.py

# Install package
RUN pip install --no-cache-dir .

# Copy built frontend files
COPY --from=app_node_prod_build --link /app/dist ./streamlit_dsfr/frontend/dist

# Copy frontend components individually
RUN \
	for component_path in $(find ./streamlit_dsfr/frontend/dist -mindepth 1 -type d -name 'st_*'); do \
		# Copy each component in the frontend folder
		component="${component_path##*/}"; \
		component_name="${component#st_}"; \
		mkdir -p "./streamlit_dsfr/frontend/${component}"; \
		cp -r "${component_path}/"* "./streamlit_dsfr/frontend/${component}"; \
		# Fix URLs to load assets
		sed -i 's#/_astro#/component/streamlit_dsfr.dsfr_default/_astro#g' \
			"./streamlit_dsfr/frontend/${component}/index.html" \
			; \
	done && \
	# Copy astro assets in the default component folder
	mkdir -p "./streamlit_dsfr/frontend/st_dsfr_default/_astro"; \
	cp -r "./streamlit_dsfr/frontend/dist/_astro/"* "./streamlit_dsfr/frontend/st_dsfr_default/_astro"; \
	# Fix URLs in assets to load other assets
	sed -i 's#/_astro#/component/streamlit_dsfr.dsfr_default/_astro#g' \
		"./streamlit_dsfr/frontend/st_dsfr_default/_astro/"*".css" \
		; \
	# Remove the dist folder
	rm -rf ./streamlit_dsfr/frontend/dist


# --
# Python CI/CD image

FROM app_python_base AS app_python_cicd

# Install build dependencies
RUN pip install --no-cache-dir --upgrade build

# Copy package files
COPY --from=app_python_prod_build --link /app .

# Build package
RUN python -m build

COPY --link --chmod=755 ./app/docker-cicd-command.sh /usr/local/bin/docker-cicd-command

CMD [ "docker-cicd-command" ]


# --
# Python Prod image

FROM app_python_base AS app_python_prod

# Copy source code
COPY --link ./app/demo .

# Copy built package
COPY --from=app_python_cicd --link /app/dist /tmp/dist

# Install dependencies
RUN pip install --no-cache-dir /tmp/dist/*.whl && \
	# Clean up
	rm -rf /tmp/dist

# Create user 'user' and group 'app'
RUN groupadd -r app && \
	useradd -lr -G app -d /app user && \
	chown -R user:app /app
USER user

# Expose port
EXPOSE ${PORT}

CMD [ "sh", "-c", "streamlit run app.py --server.port ${PORT}" ]
