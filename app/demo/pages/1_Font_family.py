import streamlit as st
from streamlit_dsfr import override_font_family

from disable_sidebar import disable_sidebar
from nav_menu import nav_menu

# ---

# Disable sidebar
disable_sidebar()

# ---

st.title('Police de caractères')

# Navigation menu
nav_menu()

# ---
st.divider()

st.markdown('DSFR utilise la police de caractères `Marianne`.')

st.header('Remplacer la police de caractères')

st.markdown("""
```python
from streamlit_dsfr import override_font_family
override_font_family()
```
""")

# CSS font family override
override_font_family()

st.header('Example')

st.markdown('#### This is a title')
st.markdown('This is a paragraph.')
