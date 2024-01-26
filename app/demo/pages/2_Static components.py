import streamlit as st
import streamlit_dsfr as stdsfr

from disable_sidebar import disable_sidebar
from nav_menu import nav_menu

# ---

st.set_page_config(
	page_title = 'Composants statiques',
)

# ---

# Disable sidebar
disable_sidebar()

# ---

st.title('Composants statiques')

# CSS font family override
stdsfr.override_font_family()

# Navigation menu
nav_menu()

# ---
st.divider()

st.header('Alertes')

with st.echo():
	stdsfr.alert('Ceci est une alerte')

with st.echo():
	stdsfr.alert('Alerte', 'Ceci est une alerte avec un titre h5', titleTag = 'h5')

with st.echo():
	stdsfr.alert('Erreur : titre du message', 'Description', type = 'error')
	stdsfr.alert('Succès de l\'envoi', 'Description', type = 'success')
	stdsfr.alert('Information : titre du message', 'Description détaillée du message', type = 'info')
	stdsfr.alert('Attention : titre du message', 'Description détaillée du message', type = 'warning')

with st.echo():
	stdsfr.alert('Information : titre de l\'information', small = True)
	stdsfr.alert('Information : titre de l\'information', type = 'success', small = True)
	stdsfr.alert('Information : titre de l\'information', type = 'error', small = True)

# ---
st.divider()

st.header('Badges')

with st.echo():
	stdsfr.badge('Ceci est un badge')

with st.echo():
	stdsfr.badge('Ceci est une erreur', type = 'error')
	stdsfr.badge('Ceci est un succès', type = 'success')
	stdsfr.badge('Ceci est un avertissement', type = 'warning')
	stdsfr.badge('Ceci est une info', type = 'info')
	stdsfr.badge('Ceci est une nouvelle', type = 'new')

with st.echo():
	stdsfr.badge('Ceci est un petit badge', small = True)

# ---
st.divider()

st.header('Fil d\'Ariane')

st.write('Le fil d\'Ariane n\'est pas supporté pour le moment.')

# stdsfr.breadcrumb('Home')
# stdsfr.breadcrumb(['Home', 'Page'])
# stdsfr.breadcrumb([('https://example.com', 'Example'), {'to': 'https://google.com', 'text': 'Google'}])
# stdsfr.breadcrumb(['Home', 'Page', ('https://example.com', 'Example'), {'to': 'https://google.com', 'text': 'Google'}])

# ---
st.divider()

st.header('Images')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composant Streamlit')

	with st.echo():
		st.image(
			'https://placekitten.com/300/200',
			caption = 'Ceci est une légende',
		)

with col_right:
	st.markdown('#### Composant DSFR')

	with st.echo():
		stdsfr.picture(
			'https://placekitten.com/300/200',
			caption = 'Ceci est une légende',
		)

col_left, col_right = st.columns(2)

with col_right:
	st.divider()

	with st.echo():
		stdsfr.picture(
			'https://placekitten.com/400/200',
			caption = 'Ceci est une légende',
			alt = 'Ceci est une description alternative',
			ratio = '32x9',
		)
