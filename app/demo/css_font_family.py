import streamlit as st

def css_font_family():
	"""
	Set CSS font family
	"""
	st.markdown(
		"""
<style>
body .stApp .appview-container * {
	font-family: Marianne, arial, sans-serif;
}
</style>
		""",
		unsafe_allow_html=True,
	)
