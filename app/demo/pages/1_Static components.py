import streamlit as st
from streamlit_dsfr import \
	dsfr_alert, \
	dsfr_badge, \
	dsfr_picture

from disable_sidebar import disable_sidebar
from css_font_family import css_font_family
from nav_menu import nav_menu

# ---

# Disable sidebar
disable_sidebar()

# ---

st.title('Composants statiques')

# CSS font family override
css_font_family()

# Navigation menu
nav_menu()

# ---
st.divider()

st.header('Alertes')

dsfr_alert('Ceci est une alerte')
dsfr_alert('Alerte', 'Ceci est une alerte avec un titre h5', titleTag = 'h5')
dsfr_alert('Erreur : titre du message', 'Description', type = 'error')
dsfr_alert('Succès de l\'envoi', 'Description', type = 'success')
dsfr_alert('Information : titre du message', 'Description détaillée du message', type = 'info')
dsfr_alert('Attention : titre du message', 'Description détaillée du message', type = 'warning')
dsfr_alert('Information : titre de l\'information', small = True)
dsfr_alert('Information : titre de l\'information', type = 'success', small = True)
dsfr_alert('Information : titre de l\'information', type = 'error', small = True)

# ---
st.divider()

st.header('Badges')

dsfr_badge('This is a badge')
dsfr_badge('This is an error', type = 'error')
dsfr_badge('This is a success', type = 'success')
dsfr_badge('This is a warning', type = 'warning')
dsfr_badge('This is an info', type = 'info')
dsfr_badge('This is a new', type = 'new')
dsfr_badge('This is a small badge', small = True)

# ---
st.divider()

st.header('Breadcrumbs')

st.write('Breadcrumbs are not supported yet.')

# dsfr_breadcrumb('Home')
# dsfr_breadcrumb(['Home', 'Page'])
# dsfr_breadcrumb([('https://example.com', 'Example'), {'to': 'https://google.com', 'text': 'Google'}])
# dsfr_breadcrumb(['Home', 'Page', ('https://example.com', 'Example'), {'to': 'https://google.com', 'text': 'Google'}])

# ---
st.divider()

st.header('Pictures')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Vanilla components')

	st.image(
		'https://placekitten.com/300/200',
		caption = 'This is a picture legend',
	)

with col_right:
	st.markdown('#### DSFR components')

	dsfr_picture(
		'https://placekitten.com/300/200',
		legend = 'This is a picture legend',
	)

	dsfr_picture(
		'https://placekitten.com/400/200',
		legend = 'This is a picture legend',
		alt = 'This is a picture alt',
		ratio = '32x9',
	)
