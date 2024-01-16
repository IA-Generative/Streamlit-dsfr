import streamlit as st
from streamlit_dsfr import \
	dsfr_button, \
	dsfr_checkbox, \
	dsfr_radio, \
	dsfr_input

# ---

st.title('Interactive components')

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

st.subheader('Radios')

val = dsfr_radio(['Option 1', 'Option 2', 'Option 3'])
st.write(val)

val = dsfr_radio(['Small option 1', 'Small option 2', 'Small option 3'], small = True)
st.write(val)

# ---

if dsfr_button('Click me'):
	st.markdown('You clicked the button')

st.markdown('---')
st.subheader('Component with variable args')

name_input = st.text_input('Enter a name', value = 'Streamlit')

if dsfr_button(name_input):
	st.markdown('You clicked the button')
