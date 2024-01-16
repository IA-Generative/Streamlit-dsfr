import math
import random

import streamlit as st
from streamlit_dsfr import \
	dsfr_button, \
	dsfr_checkbox, \
	dsfr_radio, \
	dsfr_input

from disable_sidebar import disable_sidebar
from nav_menu import nav_menu

# ---

# Disable sidebar
disable_sidebar()

# ---

st.title('Interactive components')

# Navigation menu
nav_menu()

# ---
st.divider()

st.header('Buttons')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Vanilla components:')

	val = st.button('This is a button')
	st.write(val)

	val = st.button(f'This is a random number: {math.floor(random.random() * 100)}')
	st.write(val)

with col_right:
	st.markdown('#### DSFR components:')

	val = dsfr_button('This is a button')
	st.write(val)

	val = dsfr_button(f'This is a random number: {math.floor(random.random() * 100)}')
	st.write(val)

# ---
st.divider()

st.header('Checkboxes')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Vanilla components:')

	val = st.checkbox('This is a checkbox')
	st.write(val)

with col_right:
	st.markdown('#### DSFR components:')

	val = dsfr_checkbox('This is a checkbox')
	st.write(val)

# ---
st.divider()

st.header('Inputs')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Vanilla components:')

	val = st.text_input('This is an input')
	st.write(val)

with col_right:
	st.markdown('#### DSFR components:')

	val = dsfr_input('This is an input')
	st.write(val)

# ---
st.divider()

st.header('Radios')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Vanilla components:')

	val = st.radio('This is a radio', ['Option 1', 'Option 2', 'Option 3'])
	st.write(val)

with col_right:
	st.markdown('#### DSFR components:')

	val = dsfr_radio(['Option 1', 'Option 2', 'Option 3'])
	st.write(val)

	val = dsfr_radio(['Small option 1', 'Small option 2', 'Small option 3'], small = True)
	st.write(val)

# ---
st.divider()

if dsfr_button('Click me'):
	st.markdown('You clicked the button')

st.markdown('---')
st.header('Component with variable args')

name_input = st.text_input('Enter a name', value = 'Streamlit')

if dsfr_button(name_input):
	st.markdown('You clicked the button')
