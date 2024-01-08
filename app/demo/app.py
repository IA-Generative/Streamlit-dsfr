import streamlit as st
from streamlit_dsfr import \
	dsfr_alert, \
	dsfr_badge, \
	dsfr_button, \
	dsfr_checkbox, \
	dsfr_input

# ---

st.title('Demo')

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

st.subheader('Buttons')

bval = dsfr_button('This is a button')
st.write(bval)

# ---

st.subheader('Checkboxes')

cval = dsfr_checkbox('This is a checkbox')
st.write(cval)

# ---

st.subheader('Inputs')

val = dsfr_input('This is an input')
st.write(val)

# ---

if dsfr_button('Click me'):
	st.markdown('You clicked the button')

st.markdown('---')
st.subheader('Component with variable args')

name_input = st.text_input('Enter a name', value = 'Streamlit')

if dsfr_button(name_input):
	st.markdown('You clicked the button')
