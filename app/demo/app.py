import streamlit as st
from streamlit_dsfr import \
	dsfr_alert, \
	dsfr_badge, \
	dsfr_breadcrumb, \
	dsfr_button, \
	dsfr_input

dsfr_alert('This is an alert')

dsfr_badge('This is a badge')

dsfr_breadcrumb(['Home', 'Page'])

dsfr_button('This is a button')

dsfr_input('This is an input')

if dsfr_button('Click me'):
	st.markdown('You clicked the button')

st.markdown('---')
st.subheader('Component with variable args')

name_input = st.text_input('Enter a name', value = 'Streamlit')

if dsfr_button(name_input):
	st.markdown('You clicked the button')
