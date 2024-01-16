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
This app demonstrates the use of DSFR components in Streamlit.

The app uses the [`streamlit_dsfr`](https://pypi.org/project/streamlit-dsfr/) Python package.

The packages uses [`vue-dsfr`](https://github.com/dnum-mi/vue-dsfr) components
(with the [`@gouvminint/vue-dsfr`](https://www.npmjs.com/package/@gouvminint/vue-dsfr) package).

Learn more about the DSFR design system on the [official website](https://www.systeme-de-design.gouv.fr/).
""")
