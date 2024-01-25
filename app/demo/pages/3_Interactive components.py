import math
import random

import streamlit as st
import streamlit_dsfr as stdsfr

from disable_sidebar import disable_sidebar
from nav_menu import nav_menu

# ---

# Disable sidebar
disable_sidebar()

# ---

st.title('Composants interactifs')

# CSS font family override
stdsfr.override_font_family()

# Navigation menu
nav_menu()

# ---
st.divider()

st.header('Boutons')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composant Streamlit')

	with st.echo():
		st_val = st.button('Ceci est un bouton')
		st.write('Value:', st_val)

with col_right:
	st.markdown('#### Composant DSFR')

	with st.echo():
		dsfr_val = stdsfr.button('Ceci est un bouton')
		st.write('Value:', dsfr_val)

col_left, col_right = st.columns(2)

with col_left:
	st.divider()

	with st.echo():
		st_val = st.button(
			f'Ceci est un nombre aléatoire: {math.floor(random.random() * 100)}',
			key = 'st_random_button',
		)
		st.write('Value:', st_val)

with col_right:
	st.divider()

	with st.echo():
		dsfr_val = stdsfr.button(
			f'Ceci est un nombre aléatoire: {math.floor(random.random() * 100)}',
			key = 'dsfr_random_button',
		)
		st.write('Value:', dsfr_val)

# ---
st.divider()

st.header('Boutons lien')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composants Streamlit')

	with st.echo():
		st.link_button('Ceci est un bouton lien', 'https://www.streamlit.io')

with col_right:
	st.markdown('#### Composants DSFR')

	with st.echo():
		dsfr_val = stdsfr.link_button('Ceci est un bouton lien', 'https://www.streamlit.io')
		st.write('Value:', dsfr_val)


# ---
st.divider()

st.header('Boutons copie')

st.markdown('On click, the button copies a value to the clipboard.')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composants Streamlit')

	st.markdown('Pas d\'équivalent Streamlit')

with col_right:
	st.markdown('#### Composants DSFR')

	with st.echo():
		dsfr_val = stdsfr.copy_button('Ceci est un bouton copie', 'dsfr_copy_button')
		st.write('Value:', dsfr_val)

# ---
st.divider()

st.header('Cases à cocher')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composant Streamlit')

	with st.echo():
		st_val = st.checkbox('Ceci est une case à cocher')
		st.write('Value:', st_val)

with col_right:
	st.markdown('#### Composant DSFR')

	with st.echo():
		dsfr_val = stdsfr.checkbox('Ceci est une case à cocher')
		st.write('Value:', dsfr_val)

col_left, col_right = st.columns(2)

with col_right:
	st.divider()

	with st.echo():
		dsfr_val = stdsfr.checkbox(
			'Ceci est une petite case à cocher',
			small = True,
		)
		st.write('Value:', dsfr_val)

col_left, col_right = st.columns(2)

with col_left:
	st.divider()

	with st.echo():
		st_val = st.checkbox(
			'Ceci est une case à cocher',
			help = 'Ceci est une aide',
		)
		st.write('Value:', st_val)

with col_right:
	st.divider()

	with st.echo():
		dsfr_val = stdsfr.checkbox(
			'Ceci est une case à cocher',
			help = 'Ceci est une aide',
		)
		st.write('Value:', dsfr_val)

# ---
st.divider()

st.header('Champs de saisie')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composant Streamlit')

	with st.echo():
		st_val = st.text_input('Ceci est un champ de saisie')
		st.write('Value:', st_val)

with col_right:
	st.markdown('#### Composant DSFR')

	with st.echo():
		dsfr_val = stdsfr.text_input('Ceci est un champ de saisie')
		st.write('Value:', dsfr_val)

col_left, col_right = st.columns(2)

with col_left:
	st.divider()

	with st.echo():
		st_val = st.text_input(
			'Ceci est un champ de saisie',
			help = 'Ceci est une aide',
		)
		st.write('Value:', st_val)

with col_right:
	st.divider()

	with st.echo():
		dsfr_val = stdsfr.text_input(
			'Ceci est un champ de saisie',
			help = 'Ceci est une aide',
		)
		st.write('Value:', dsfr_val)

col_left, col_right = st.columns(2)

with col_left:
	st.divider()

	with st.echo():
		st_val = st.number_input('Ceci est un champ de saisie numérique')
		st.write('Value:', st_val)

with col_right:
	st.divider()

	with st.echo():
		dsfr_val = stdsfr.number_input('Ceci est un champ de saisie numérique')
		st.write('Value:', dsfr_val)

col_left, col_right = st.columns(2)

with col_left:
	st.divider()

	with st.echo():
		st_val = st.text_area('Ceci est une zone de texte')
		st.write('Value:', st_val)

with col_right:
	st.divider()

	with st.echo():
		dsfr_val = stdsfr.text_area('Ceci est une zone de texte')
		st.write('Value:', dsfr_val)

# WIP
col_left, col_right = st.columns(2)

with col_left:
	st.divider()

	with st.echo():
		st_val = st.date_input('Ceci est un champ de saisie de date')
		st.write('Value:', st_val)

with col_right:
	st.divider()

	with st.echo():
		dsfr_val = stdsfr.date_input('Ceci est un champ de saisie de date')
		st.write('Value:', dsfr_val)

# WIP
col_left, col_right = st.columns(2)

with col_left:
	st.divider()

	with st.echo():
		st_val = st.time_input('Ceci est un champ de saisie de temps')
		st.write('Value:', st_val)

with col_right:
	st.divider()

	with st.echo():
		dsfr_val = stdsfr.time_input('Ceci est un champ de saisie de temps')
		st.write('Value:', dsfr_val)

# ---
st.divider()

st.header('Boutons radio')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composant Streamlit')

	with st.echo():
		st_val = st.radio(
			'Ceci sont des boutons radio',
			['Option 1', 'Option 2 (default)', 'Option 3'],
			1,
		)
		st.write('Value:', st_val)

with col_right:
	st.markdown('#### Composant DSFR')

	with st.echo():
		dsfr_val = stdsfr.radio(
			'Ceci sont des boutons radio',
			['Option 1', 'Option 2 (default)', 'Option 3'],
			1,
		)
		st.write('Value:', dsfr_val)

col_left, col_right = st.columns(2)

with col_right:
	st.divider()

	with st.echo():
		dsfr_val = stdsfr.radio(
			'Ceci sont des petits boutons radio',
			['Small option 1', 'Small option 2', 'Small option 3'],
			small = True,
		)
		st.write('Value:', dsfr_val)

col_left, col_right = st.columns(2)

with col_left:
	st.divider()

	with st.echo():
		st_val = st.radio(
			'Ceci sont des boutons radio',
			['Option 1', 'Option 2', 'Option 3'],
			format_func = lambda x: str(x) + '!',
		)
		st.write('Value:', st_val)

with col_right:
	st.divider()

	with st.echo():
		dsfr_val = stdsfr.radio(
			'Ceci sont des petits boutons radio',
			['Option 1', 'Option 2', 'Option 3'],
			format_func = lambda x: str(x) + '!',
		)
		st.write('Value:', dsfr_val)

# ---
st.divider()

st.header('Curseur')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composant Streamlit')

	with st.echo():
		st_val = st.slider('Ceci est un curseur')
		st.write('Value:', st_val)

with col_right:
	st.markdown('#### Composant DSFR')

	with st.echo():
		dsfr_val = stdsfr.range('Ceci est un curseur')
		st.write('Value:', dsfr_val)

col_left, col_right = st.columns(2)

with col_left:
	st.divider()

	with st.echo():
		st_val = st.slider('Ceci est un curseur', 0, 100, 50)
		st.write('Value:', st_val)

with col_right:
	st.divider()

	with st.echo():
		dsfr_val = stdsfr.range('Ceci est un curseur', 0, 100, 50, small = True)
		st.write('Value:', dsfr_val)

# ---
st.divider()

st.header('Téléversement de fichier')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composants Streamlit')

	with st.echo():
		st_val = st.file_uploader(
			'Ceci est un téléversement de fichier',
		)
		st.write('Value:', st_val)

with col_right:
	st.markdown('#### Composants DSFR')

	with st.echo():
		dsfr_val = stdsfr.file_uploader(
			'Ceci est un téléversement de fichier',
		)
		st.write('Value:', dsfr_val)

col_left, col_right = st.columns(2)

with col_left:
	st.divider()

	with st.echo():
		st_val = st.file_uploader(
			'Ceci est un téléversement de plusieurs fichiers',
			accept_multiple_files = True,
		)
		st.write('Value:', st_val)

with col_right:
	st.divider()

	# DSFR component does not support multiple files upload
	st.write('Le composant DSFR ne permet pas de téléverser plusieurs fichiers')
