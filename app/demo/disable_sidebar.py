import streamlit as st

def disable_sidebar():
	"""
	Disable sidebar in Streamlit page.
	"""
	st.markdown(
		"""
<style>
	[data-testid="stSidebar"],
	[data-testid="collapsedControl"] {
		display: none;
	}
</style>
		""",
		unsafe_allow_html=True,
	)
