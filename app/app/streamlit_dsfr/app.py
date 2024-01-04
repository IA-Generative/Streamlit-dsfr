import streamlit as st
from __init__ import my_component, dsfr_button

# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/example.py`

st.subheader('Component with constant args')

# Create an instance of our component with a constant `name` arg, and
# print its output value.
num_clicks = my_component('World')
st.markdown(f'You\'ve clicked {int(num_clicks)} times!')

if dsfr_button('Click me'):
	st.markdown('You clicked the button')

st.markdown('---')
st.subheader('Component with variable args')

# Create a second instance of our component whose `name` arg will vary
# based on a text_input widget.
#
# We use the special "key" argument to assign a fixed identity to this
# component instance. By default, when a component's arguments change,
# it is considered a new instance and will be re-mounted on the frontend
# and lose its current state. In this case, we want to vary the component's
# "name" argument without having it get recreated.
name_input = st.text_input('Enter a name', value = 'Streamlit')
num_clicks = my_component(name_input, key = 'foo')
st.markdown(f'You\'ve clicked {int(num_clicks)} times!')

if dsfr_button(name_input):
	st.markdown('You clicked the button')
