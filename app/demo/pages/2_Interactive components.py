import math
import random

import streamlit as st
from streamlit_dsfr import \
	dsfr_button, \
	dsfr_checkbox, \
	dsfr_radio, \
	dsfr_input

from disable_sidebar import disable_sidebar
from css_font_family import css_font_family
from nav_menu import nav_menu

# ---

# Disable sidebar
disable_sidebar()

# ---

st.title('Composants interactifs')

# CSS font family override
css_font_family()

# Navigation menu
nav_menu()

# ---
st.divider()

st.header('Boutons')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composants vanilla')

	st_val = st.button('Ceci est un bouton')
	st.write(st_val)

	st_val = st.button(
		f'Ceci est un nombre aléatoire: {math.floor(random.random() * 100)}',
		key = 'st_random_button',
	)
	st.write(st_val)

with col_right:
	st.markdown('#### Composants DSFR')

	dsfr_val = dsfr_button('Ceci est un bouton')
	st.write(dsfr_val)

	dsfr_val = dsfr_button(
		f'Ceci est un nombre aléatoire: {math.floor(random.random() * 100)}',
		key = 'dsfr_random_button',
	)
	st.write(dsfr_val)

# ---
st.divider()

st.header('Cases à cocher')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composants vanilla')

	st_val = st.checkbox('Ceci est une case à cocher')
	st.write(st_val)

with col_right:
	st.markdown('#### Composants DSFR')

	dsfr_val = dsfr_checkbox('Ceci est une case à cocher')
	st.write(dsfr_val)

# ---
st.divider()

st.header('Champs de saisie')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composants vanilla')

	st_val = st.text_input('Ceci est un champ de saisie')
	st.write(st_val)

with col_right:
	st.markdown('#### Composants DSFR')

	dsfr_val = dsfr_input('Ceci est un champ de saisie')
	st.write(dsfr_val)

# ---
st.divider()

st.header('Boutons radio')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composants vanilla')

	st_val = st.radio('Ceci sont des boutons radio', ['Option 1', 'Option 2', 'Option 3'])
	st.write(st_val)

with col_right:
	st.markdown('#### Composants DSFR')

	dsfr_val = dsfr_radio(['Option 1', 'Option 2', 'Option 3'])
	st.write(dsfr_val)

	dsfr_val = dsfr_radio(['Small option 1', 'Small option 2', 'Small option 3'], small = True)
	st.write(dsfr_val)

# ---
st.divider()

if dsfr_button('Cliquez moi'):
	st.markdown('Vous avez cliqué sur le bouton')

st.markdown('---')
st.header('Composant avec des arguments variables')

name_input = st.text_input('Entrez un nom', value = 'Streamlit')

if dsfr_button(name_input):
	st.markdown('Vous avez cliqué sur le bouton')
