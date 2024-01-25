# streamlit-dsfr

VueDsfr components for Streamlit


## Installation instructions

```sh
pip install streamlit-dsfr
```


## Usage instructions

```python
import streamlit as st
import streamlit_dsfr as stdsfr

# Instead of st.button():
value = stdsfr.button()

# Returns True or False
st.write(value)
```

Available static components:
- `dsfr_alert`
- `dsfr_badge`
- `dsfr_picture`

Available interactive components:
- `dsfr_button`
- `dsfr_checkbox`
- `dsfr_radio`
- `dsfr_text_input`
- `dsfr_number_input`
- `dsfr_text_area`
- `dsfr_range`
