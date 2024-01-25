import streamlit as st

def nav_menu():
	"""
	Print navigation menu.
	"""
	st.markdown(
		"""
- <a href="Font_family" target="_self">Police de caractères</a>
- <a href="Static_components" target="_self">Composants statiques</a>
- <a href="Interactive_components" target="_self">Composants interactifs</a>
		""",
		unsafe_allow_html = True,
	)
