import streamlit as st

from disable_sidebar import disable_sidebar
from nav_menu import nav_menu

# ---

# Disable sidebar
disable_sidebar()

# ---

st.title('DSFR components demo')

# Navigation menu
nav_menu()
