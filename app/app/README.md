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
