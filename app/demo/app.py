import streamlit as st
from streamlit_dsfr import \
	dsfr_alert, \
	dsfr_badge, \
	dsfr_breadcrumb, \
	dsfr_button, \
	dsfr_input

dsfr_alert('This is an alert')

dsfr_badge('This is a badge')

dsfr_breadcrumb(['Home', 'Page', ('https://example.com', 'Example'), {'to': 'https://google.com', 'link': 'Google'}])

bval = dsfr_button('This is a button')
st.write(bval)

val = dsfr_input('This is an input')
st.write(val)

if dsfr_button('Click me'):
	st.markdown('You clicked the button')

st.markdown('---')
st.subheader('Component with variable args')

name_input = st.text_input('Enter a name', value = 'Streamlit')

if dsfr_button(name_input):
	st.markdown('You clicked the button')
