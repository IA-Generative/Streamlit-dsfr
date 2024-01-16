import streamlit as st
from streamlit_dsfr import \
	dsfr_alert, \
	dsfr_badge, \
	dsfr_picture

from disable_sidebar import disable_sidebar
from nav_menu import nav_menu

# ---

# Disable sidebar
disable_sidebar()

# ---

st.title('Static components')

# Navigation menu
nav_menu()

# ---

st.subheader('Alerts')

dsfr_alert('This is an alert')
dsfr_alert('Alert', 'This is an alert with a title')
dsfr_alert('Alert', 'This is an alert with an h3 title', titleTag = 'h3')
dsfr_alert('This is an error', type = 'error')
dsfr_alert('This is a success', type = 'success')
dsfr_alert('This is a warning', type = 'warning')
dsfr_alert('This is an info', type = 'info')
dsfr_alert('This is a small alert', small = True)

# ---

st.subheader('Badges')

dsfr_badge('This is a badge')
dsfr_badge('This is an error', type = 'error')
dsfr_badge('This is a success', type = 'success')
dsfr_badge('This is a warning', type = 'warning')
dsfr_badge('This is an info', type = 'info')
dsfr_badge('This is a new', type = 'new')
dsfr_badge('This is a small badge', small = True)

# ---

st.subheader('Breadcrumbs')

st.write('Breadcrumbs are not supported yet.')

# dsfr_breadcrumb('Home')
# dsfr_breadcrumb(['Home', 'Page'])
# dsfr_breadcrumb([('https://example.com', 'Example'), {'to': 'https://google.com', 'text': 'Google'}])
# dsfr_breadcrumb(['Home', 'Page', ('https://example.com', 'Example'), {'to': 'https://google.com', 'text': 'Google'}])

# ---

st.subheader('Pictures')

dsfr_picture(
	'https://placekitten.com/640/180', # 32x9 ratio
	legend = 'This is a picture legend',
	alt = 'This is a picture alt',
	ratio = '32x9',
)
