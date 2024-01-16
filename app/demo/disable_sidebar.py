import streamlit as st

def disable_sidebar():
	"""
	Disable sidebar in Streamlit page.
	"""
	st.set_page_config(initial_sidebar_state="collapsed")
	st.markdown(
		"""
<style>
	[data-testid="collapsedControl"] {
		display: none;
	}
</style>
		""",
		unsafe_allow_html=True,
	)
