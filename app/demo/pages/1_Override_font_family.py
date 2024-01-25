import streamlit as st
from streamlit_dsfr import override_font_family

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

# CSS font family override
override_font_family()

st.markdown('### This is a title')
st.markdown('This is a paragraph.')
