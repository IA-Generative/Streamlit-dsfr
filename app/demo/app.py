import streamlit as st

from disable_sidebar import disable_sidebar
from css_font_family import css_font_family
from nav_menu import nav_menu

# ---

# Disable sidebar
disable_sidebar()

# ---

st.title('DSFR components demo')

# CSS font family override
css_font_family()

# Navigation menu
nav_menu()
