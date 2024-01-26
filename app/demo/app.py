import streamlit as st
import streamlit_dsfr as stdsfr

from disable_sidebar import disable_sidebar
from nav_menu import nav_menu

# ---

st.set_page_config(
	page_title = 'Demo Streamlit DSFR',
)

# ---

# Disable sidebar
disable_sidebar()

# ---

st.title('Demo Streamlit DSFR')

# CSS font family override
stdsfr.override_font_family()

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
