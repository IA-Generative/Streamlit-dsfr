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
- `stdsfr.alert`
- `stdsfr.badge`
- `stdsfr.image`

Available interactive components:
- `stdsfr.button`
- `stdsfr.link_button`
- `stdsfr.copy_button`
- `stdsfr.checkbox`
- `stdsfr.radio`
- `stdsfr.text_input`
- `stdsfr.number_input`
- `stdsfr.text_area`
- `stdsfr.slider`
- `stdsfr.file_uploader`
