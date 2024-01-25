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

	with st.echo('below'):
		st_val = st.button('Ceci est un bouton')
		st.write(st_val)

with col_right:
	st.markdown('#### Composant DSFR')

	with st.echo('below'):
		dsfr_val = stdsfr.button('Ceci est un bouton')
		st.write(dsfr_val)

col_left, col_right = st.columns(2)

with col_left:
	with st.echo('below'):
		st_val = st.button(
			f'Ceci est un nombre aléatoire: {math.floor(random.random() * 100)}',
			key = 'st_random_button',
		)
		st.write(st_val)

with col_right:
	with st.echo('below'):
		dsfr_val = stdsfr.button(
			f'Ceci est un nombre aléatoire: {math.floor(random.random() * 100)}',
			key = 'dsfr_random_button',
		)
		st.write(dsfr_val)

# ---
st.divider()

st.header('Boutons lien')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composants Streamlit')

	st.link_button('Ceci est un bouton lien', 'https://www.streamlit.io')

with col_right:
	st.markdown('#### Composants DSFR')

	stdsfr.link_button('Ceci est un bouton lien', 'https://www.streamlit.io')

# ---
st.divider()

st.header('Boutons copie')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composants Streamlit')

	st.markdown('Pas d\'équivalent Streamlit')

with col_right:
	st.markdown('#### Composants DSFR')

	stdsfr.copy_button('Ceci est un bouton copie', 'dsfr_copy_button')

# ---
st.divider()

st.header('Cases à cocher')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composant Streamlit')

	with st.echo('below'):
		st_val = st.checkbox('Ceci est une case à cocher')
		st.write(st_val)

with col_right:
	st.markdown('#### Composant DSFR')

	with st.echo('below'):
		dsfr_val = stdsfr.checkbox('Ceci est une case à cocher')
		st.write(dsfr_val)

col_left, col_right = st.columns(2)

with col_right:
	with st.echo('below'):
		dsfr_val = stdsfr.checkbox(
			'Ceci est une petite case à cocher',
			small = True,
		)
		st.write(dsfr_val)

col_left, col_right = st.columns(2)

with col_left:
	with st.echo('below'):
		st_val = st.checkbox(
			'Ceci est une case à cocher',
			help = 'Ceci est une aide',
		)
		st.write(st_val)

with col_right:
	with st.echo('below'):
		dsfr_val = stdsfr.checkbox(
			'Ceci est une case à cocher',
			help = 'Ceci est une aide',
		)
		st.write(dsfr_val)

# ---
st.divider()

st.header('Champs de saisie')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composant Streamlit')

	with st.echo('below'):
		st_val = st.text_input('Ceci est un champ de saisie')
		st.write(st_val)

with col_right:
	st.markdown('#### Composant DSFR')

	with st.echo('below'):
		dsfr_val = stdsfr.text_input('Ceci est un champ de saisie')
		st.write(dsfr_val)

col_left, col_right = st.columns(2)

with col_left:
	with st.echo('below'):
		st_val = st.text_input(
			'Ceci est un champ de saisie',
			help = 'Ceci est une aide',
		)
		st.write(st_val)

with col_right:
	with st.echo('below'):
		dsfr_val = stdsfr.text_input(
			'Ceci est un champ de saisie',
			help = 'Ceci est une aide',
		)
		st.write(dsfr_val)

col_left, col_right = st.columns(2)

with col_left:
	with st.echo('below'):
		st_val = st.number_input('Ceci est un champ de saisie numérique')
		st.write(st_val)

with col_right:
	with st.echo('below'):
		dsfr_val = stdsfr.number_input('Ceci est un champ de saisie numérique')
		st.write(dsfr_val)

col_left, col_right = st.columns(2)

with col_left:
	with st.echo('below'):
		st_val = st.text_area('Ceci est une zone de texte')
		st.write(st_val)

with col_right:
	with st.echo('below'):
		dsfr_val = stdsfr.text_area('Ceci est une zone de texte')
		st.write(dsfr_val)

# WIP
col_left, col_right = st.columns(2)

with col_left:
	with st.echo('below'):
		st_val = st.date_input('Ceci est un champ de saisie de date')
		st.write(st_val)

with col_right:
	with st.echo('below'):
		dsfr_val = stdsfr.date_input('Ceci est un champ de saisie de date')
		st.write(dsfr_val)

# WIP
col_left, col_right = st.columns(2)

with col_left:
	with st.echo('below'):
		st_val = st.time_input('Ceci est un champ de saisie de temps')
		st.write(st_val)

with col_right:
	with st.echo('below'):
		dsfr_val = stdsfr.time_input('Ceci est un champ de saisie de temps')
		st.write(dsfr_val)

# ---
st.divider()

st.header('Boutons radio')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composant Streamlit')

	with st.echo('below'):
		st_val = st.radio(
			'Ceci sont des boutons radio',
			['Option 1', 'Option 2 (default)', 'Option 3'],
			1,
		)
		st.write(st_val)

with col_right:
	st.markdown('#### Composant DSFR')

	with st.echo('below'):
		dsfr_val = stdsfr.radio(
			'Ceci sont des boutons radio',
			['Option 1', 'Option 2 (default)', 'Option 3'],
			1,
		)
		st.write(dsfr_val)

col_left, col_right = st.columns(2)

with col_right:
	with st.echo('below'):
		dsfr_val = stdsfr.radio(
			'Ceci sont des petits boutons radio',
			['Small option 1', 'Small option 2', 'Small option 3'],
			small = True,
		)
		st.write(dsfr_val)

# ---
st.divider()

st.header('Curseur')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composant Streamlit')

	with st.echo('below'):
		st_val = st.slider('Ceci est un curseur')
		st.write(st_val)

with col_right:
	st.markdown('#### Composant DSFR')

	with st.echo('below'):
		dsfr_val = stdsfr.range('Ceci est un curseur')
		st.write(dsfr_val)

col_left, col_right = st.columns(2)

with col_left:
	with st.echo('below'):
		st_val = st.slider('Ceci est un curseur', 0, 100, 50)
		st.write(st_val)

with col_right:
	with st.echo('below'):
		dsfr_val = stdsfr.range('Ceci est un curseur', 0, 100, 50, small = True)
		st.write(dsfr_val)

# ---
st.divider()

st.header('Téléversement de fichier')

col_left, col_right = st.columns(2)

with col_left:
	st.markdown('#### Composants Streamlit')

	with st.echo('below'):
		st_val = st.file_uploader(
			'Ceci est un téléversement de fichier',
		)
		st.write(st_val)

with col_right:
	st.markdown('#### Composants DSFR')

	with st.echo('below'):
		dsfr_val = stdsfr.file_uploader(
			'Ceci est un téléversement de fichier',
		)
		st.write(dsfr_val)

col_left, col_right = st.columns(2)

with col_left:
	with st.echo('below'):
		st_val = st.file_uploader(
			'Ceci est un téléversement de plusieurs fichiers',
			accept_multiple_files = True,
		)
		st.write(st_val)

with col_right:
	# DSFR component does not support multiple files upload
	st.write('Le composant DSFR ne permet pas de téléverser plusieurs fichiers')
