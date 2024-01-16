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

# ---
st.divider()

st.markdown("""
Cette application présente l'utilisation des composants DSFR dans Streamlit.

L'application utilise le package Python
[`streamlit_dsfr`](https://pypi.org/project/streamlit-dsfr/).

Le package utilise les composants [`vue-dsfr`](https://github.com/dnum-mi/vue-dsfr)
(avec le package [`@gouvminint/vue-dsfr`](https://www.npmjs.com/package/@gouvminint/vue-dsfr)).

Plus d'informations sur le design system DSFR sur le
[site officiel](https://www.systeme-de-design.gouv.fr/).
""")
