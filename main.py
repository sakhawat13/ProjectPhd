


import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
from st_aggrid.shared import JsCode




# In[3]:

from typing import Union, Dict
from io import BytesIO, StringIO
import json
import pandas as pd
import requests
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

df = pd.read_excel("https://www2.census.gov/programs-surveys/mhs/tables/2022/puf2022.xls")
st.set_page_config(
    layout="wide"
)
tab1, tab2, tab3 = st.tabs(["Metric", "Overview", "Code"])

with tab2:
    st.title("Report")
    pr = df.profile_report()
    st_profile_report(pr)
with tab1:
    st.title("Measurements")
    st.metric(label="Total number of phd granting institutes", value="2000")
    st.metric(label="Missing people with hindex>5 ", value="2000")

with tab3:
    with st.expander("See Logic"):
        st.write("Here are some logics:")

    code = '''def hello():
    print("Hello, Streamlit!")'''
    st.code(code, language='python')

# In[4]:






