import streamlit as st

def override_font_family():
	"""
	Set CSS font family
	"""
	st.markdown(
		"""
<style>
@font-face {
    font-display: swap;
    font-family: Marianne;
    font-style: normal;
    font-weight: 300;
    src: url(/component/streamlit_dsfr.dsfr_default/_astro/Marianne-Light.7GX88oPX.woff2) format("woff2"),url(/component/streamlit_dsfr.dsfr_default/_astro/Marianne-Light.6lmsSnc8.woff) format("woff")
}
@font-face {
    font-display: swap;
    font-family: Marianne;
    font-style: italic;
    font-weight: 300;
    src: url(/component/streamlit_dsfr.dsfr_default/_astro/Marianne-Light_Italic.GJ3thv45.woff2) format("woff2"),url(/component/streamlit_dsfr.dsfr_default/_astro/Marianne-Light_Italic.STgl0sbt.woff) format("woff")
}
@font-face {
    font-display: swap;
    font-family: Marianne;
    font-style: normal;
    font-weight: 400;
    src: url(/component/streamlit_dsfr.dsfr_default/_astro/Marianne-Regular.mgqq5yTO.woff2) format("woff2"),url(/component/streamlit_dsfr.dsfr_default/_astro/Marianne-Regular.8SHksZge.woff) format("woff")
}
@font-face {
    font-display: swap;
    font-family: Marianne;
    font-style: italic;
    font-weight: 400;
    src: url(/component/streamlit_dsfr.dsfr_default/_astro/Marianne-Regular_Italic.3R_BbTaN.woff2) format("woff2"),url(/component/streamlit_dsfr.dsfr_default/_astro/Marianne-Regular_Italic.UCbE0jax.woff) format("woff")
}
@font-face {
    font-display: swap;
    font-family: Marianne;
    font-style: normal;
    font-weight: 500;
    src: url(/component/streamlit_dsfr.dsfr_default/_astro/Marianne-Medium.A6bVQEda.woff2) format("woff2"),url(/component/streamlit_dsfr.dsfr_default/_astro/Marianne-Medium.prCK3SSS.woff) format("woff")
}
@font-face {
    font-display: swap;
    font-family: Marianne;
    font-style: italic;
    font-weight: 500;
    src: url(/component/streamlit_dsfr.dsfr_default/_astro/Marianne-Medium_Italic.FqmRU-8D.woff2) format("woff2"),url(/component/streamlit_dsfr.dsfr_default/_astro/Marianne-Medium_Italic.T_DBs5K5.woff) format("woff")
}
@font-face {
    font-display: swap;
    font-family: Marianne;
    font-style: normal;
    font-weight: 700;
    src: url(/component/streamlit_dsfr.dsfr_default/_astro/Marianne-Bold.mI04Wx9M.woff2) format("woff2"),url(/component/streamlit_dsfr.dsfr_default/_astro/Marianne-Bold.Lusn3uPo.woff) format("woff")
}
@font-face {
    font-display: swap;
    font-family: Marianne;
    font-style: italic;
    font-weight: 700;
    src: url(/component/streamlit_dsfr.dsfr_default/_astro/Marianne-Bold_Italic.alvVdTYc.woff2) format("woff2"),url(/component/streamlit_dsfr.dsfr_default/_astro/Marianne-Bold_Italic.VpzzqYz6.woff) format("woff")
}
@font-face {
    font-display: swap;
    font-family: Spectral;
    font-style: normal;
    font-weight: 400;
    src: url(/component/streamlit_dsfr.dsfr_default/_astro/Spectral-Regular.D5gUInLE.woff2) format("woff2"),url(/component/streamlit_dsfr.dsfr_default/_astro/Spectral-Regular.9CKHJdJx.woff) format("woff")
}
@font-face {
    font-display: swap;
    font-family: Spectral;
    font-style: normal;
    font-weight: 900;
    src: url(/component/streamlit_dsfr.dsfr_default/_astro/Spectral-ExtraBold.gs3wZvgE.woff2) format("woff2"),url(/component/streamlit_dsfr.dsfr_default/_astro/Spectral-ExtraBold.FN9ubN3N.woff) format("woff")
}

body .stApp .appview-container * {
	font-family: Marianne, arial, sans-serif;
}
</style>
		""",
		unsafe_allow_html=True,
	)
