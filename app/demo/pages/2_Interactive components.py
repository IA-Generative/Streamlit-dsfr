import math
import random

import streamlit as st
from streamlit_dsfr import \
	dsfr_button, \
	dsfr_checkbox, \
	dsfr_radio, \
	dsfr_text_input, \
	dsfr_number_input, \
	dsfr_text_area, \
	dsfr_date_input, \
	dsfr_time_input, \
	dsfr_range, \
	override_font_family

from disable_sidebar import disable_sidebar
from nav_menu import nav_menu

# ---

# Disable sidebar
disable_sidebar()

# ---

st.title('Composants interactifs')

# CSS font family override
override_font_family()

# Navigation menu
nav_menu()

# ---
st.divider()

st.header('Boutons')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composants Streamlit')

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
	st.markdown('#### Composants Streamlit')

	st_val = st.checkbox('Ceci est une case à cocher')
	st.write(st_val)

	st_val = st.checkbox(
		'Ceci est une case à cocher',
		help = 'Ceci est une aide',
	)
	st.write(st_val)

with col_right:
	st.markdown('#### Composants DSFR')

	dsfr_val = dsfr_checkbox('Ceci est une case à cocher')
	st.write(dsfr_val)

	dsfr_val = dsfr_checkbox(
		'Ceci est une case à cocher',
		help = 'Ceci est une aide',
	)
	st.write(dsfr_val)

	dsfr_val = dsfr_checkbox(
		'Ceci est une petite case à cocher',
		small = True,
	)
	st.write(dsfr_val)

# ---
st.divider()

st.header('Champs de saisie')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composants Streamlit')

	st_val = st.text_input('Ceci est un champ de saisie')
	st.write(st_val)

	st_val = st.text_input(
		'Ceci est un champ de saisie',
		help = 'Ceci est une aide',
	)
	st.write(st_val)

	st_val = st.number_input('Ceci est un champ de saisie numérique')
	st.write(st_val)

	st_val = st.text_area('Ceci est une zone de texte')
	st.write(st_val)

	st_val = st.date_input('Ceci est un champ de saisie de date')
	st.write(st_val)

	st_val = st.time_input('Ceci est un champ de saisie de temps')
	st.write(st_val)

with col_right:
	st.markdown('#### Composants DSFR')

	dsfr_val = dsfr_text_input('Ceci est un champ de saisie')
	st.write(dsfr_val)

	dsfr_val = dsfr_text_input(
		'Ceci est un champ de saisie',
		help = 'Ceci est une aide',
	)
	st.write(dsfr_val)

	dsfr_val = dsfr_number_input('Ceci est un champ de saisie numérique')
	st.write(dsfr_val)

	dsfr_val = dsfr_text_area('Ceci est une zone de texte')
	st.write(dsfr_val)

	dsfr_val = dsfr_date_input('Ceci est un champ de saisie de date')
	st.write(dsfr_val)

	dsfr_val = dsfr_time_input('Ceci est un champ de saisie de temps')
	st.write(dsfr_val)

# ---
st.divider()

st.header('Boutons radio')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composants Streamlit')

	st_val = st.radio('Ceci sont des boutons radio', ['Option 1', 'Option 2 (default)', 'Option 3'], 1)
	st.write(st_val)

with col_right:
	st.markdown('#### Composants DSFR')

	dsfr_val = dsfr_radio('Ceci sont des boutons radio', ['Option 1', 'Option 2 (default)', 'Option 3'], 1)
	st.write(dsfr_val)

	dsfr_val = dsfr_radio('Ceci sont des petits boutons radio', ['Small option 1', 'Small option 2', 'Small option 3'], small = True)
	st.write(dsfr_val)

# ---
st.divider()

st.header('Curseur')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composants Streamlit')

	st_val = st.slider('Ceci est un curseur')
	st.write(st_val)

	st_val = st.slider('Ceci est un curseur', 0, 100, 50)
	st.write(st_val)

with col_right:
	st.markdown('#### Composants DSFR')

	dsfr_val = dsfr_range('Ceci est un curseur')
	st.write(dsfr_val)

	dsfr_val = dsfr_range('Ceci est un curseur', 0, 100, 50, small = True)
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
