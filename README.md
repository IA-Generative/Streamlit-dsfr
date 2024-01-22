# Streamlit DSFR

VueDsfr components for Streamlit


## Installation instructions

```sh
pip install streamlit-dsfr
```


## Usage instructions

```python
import streamlit as st
from streamlit_dsfr import st_dsfr_button

value = st_dsfr_button()
st.write(value)
```


## Development instructions

Test the component in a production environment:

```sh
docker compose -f docker-compose.yml up --build -d
```

Test the component in a development environment:

```sh
docker compose up --build -d
```

Update the frontend packages:

```sh
docker compose -f docker-compose-npm.yml run --build --rm npm install
```


## Credits

This repository uses code from:
- [streamlit/component-template](https://github.com/streamlit/component-template), licensed under the [Apache License 2.0](https://github.com/streamlit/component-template/blob/master/LICENSE).
- [andfanilo/streamlit-component-template-vue](https://github.com/andfanilo/streamlit-component-template-vue), licensed under the [MIT License](https://github.com/andfanilo/streamlit-component-template-vue/blob/vue3/LICENSE).
