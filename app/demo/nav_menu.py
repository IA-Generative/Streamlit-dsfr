import streamlit as st

def nav_menu():
	"""
	Print navigation menu.
	"""
	st.markdown(
		"""
- <a href="Static_components" target="_self">Static components</a>
- <a href="Interactive_components" target="_self">Interactive components</a>
		""",
		unsafe_allow_html = True,
	)
