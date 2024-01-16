import streamlit as st

from disable_sidebar import disable_sidebar

# ---

# Disable sidebar
disable_sidebar()

# ---

st.title('DSFR components demo')

st.markdown(
	"""
- <a href="Static_components">Static components</a>
- <a href="Interactive_components">Interactive components</a>
	""",
	unsafe_allow_html = True,
)
