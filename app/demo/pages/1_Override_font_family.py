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

st.title('Remplacer la police de caractères')

# Navigation menu
nav_menu()

# ---
st.divider()

with st.echo():
	# CSS font family override
	override_font_family()

	st.markdown('### This is a title')
	st.markdown('This is a paragraph.')
