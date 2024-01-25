import streamlit as st
from streamlit_dsfr import \
	dsfr_alert, \
	dsfr_badge, \
	dsfr_picture, \
	override_font_family

from disable_sidebar import disable_sidebar
from nav_menu import nav_menu

# ---

# Disable sidebar
disable_sidebar()

# ---

st.title('Composants statiques')

# CSS font family override
override_font_family()

# Navigation menu
nav_menu()

# ---
st.divider()

st.header('Alertes')

with st.echo('below'):
	dsfr_alert('Ceci est une alerte')

with st.echo('below'):
	dsfr_alert('Alerte', 'Ceci est une alerte avec un titre h5', titleTag = 'h5')

with st.echo('below'):
	dsfr_alert('Erreur : titre du message', 'Description', type = 'error')
	dsfr_alert('Succès de l\'envoi', 'Description', type = 'success')
	dsfr_alert('Information : titre du message', 'Description détaillée du message', type = 'info')
	dsfr_alert('Attention : titre du message', 'Description détaillée du message', type = 'warning')

with st.echo('below'):
	dsfr_alert('Information : titre de l\'information', small = True)
	dsfr_alert('Information : titre de l\'information', type = 'success', small = True)
	dsfr_alert('Information : titre de l\'information', type = 'error', small = True)

# ---
st.divider()

st.header('Badges')

with st.echo('below'):
	dsfr_badge('Ceci est un badge')

with st.echo('below'):
	dsfr_badge('Ceci est une erreur', type = 'error')
	dsfr_badge('Ceci est un succès', type = 'success')
	dsfr_badge('Ceci est un avertissement', type = 'warning')
	dsfr_badge('Ceci est une info', type = 'info')
	dsfr_badge('Ceci est une nouvelle', type = 'new')

with st.echo('below'):
	dsfr_badge('Ceci est un petit badge', small = True)

# ---
st.divider()

st.header('Fil d\'Ariane')

st.write('Le fil d\'Ariane n\'est pas supporté pour le moment.')

# dsfr_breadcrumb('Home')
# dsfr_breadcrumb(['Home', 'Page'])
# dsfr_breadcrumb([('https://example.com', 'Example'), {'to': 'https://google.com', 'text': 'Google'}])
# dsfr_breadcrumb(['Home', 'Page', ('https://example.com', 'Example'), {'to': 'https://google.com', 'text': 'Google'}])

# ---
st.divider()

st.header('Images')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composants Streamlit')

	with st.echo('below'):
		st.image(
			'https://placekitten.com/300/200',
			caption = 'Ceci est une légende',
		)

with col_right:
	st.markdown('#### Composants DSFR')

	with st.echo('below'):
		dsfr_picture(
			'https://placekitten.com/300/200',
			caption = 'Ceci est une légende',
		)

	with st.echo('below'):
		dsfr_picture(
			'https://placekitten.com/400/200',
			caption = 'Ceci est une légende',
			alt = 'Ceci est une description alternative',
			ratio = '32x9',
		)
