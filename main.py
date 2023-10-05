


import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
from st_aggrid.shared import JsCode


import streamlit.components.v1 as components

# In[3]:

from typing import Union, Dict
from io import BytesIO, StringIO
import json
import pandas as pd
import requests
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from PIL import Image
import webbrowser


# df = pd.read_excel("https://www2.census.gov/programs-surveys/mhs/tables/2022/puf2022.xls")
st.set_page_config(
    layout="wide"
)

text = (" :white_check_mark: 1. Get PhD granting university for the top 100~  \n "
        ":white_check_mark: 2. Find all the authors' phd granting uni whose :blue[hindex> 5]  \n "
        ":white_check_mark: 3. Find authors' phd granting uni who joined program after starting career  ")
f = open("PhdGrantingInst Description.txt", encoding="utf8")


tab1, tab2, tab3 = st.tabs(["Metric", "Download", "Code"])


with tab2:

    col21, col22 = st.columns(2)
    with col21:
        st.warning('Last updated October 4th 2023', icon="🚨")

        st.write(
            "Google Drive Folder [link](https://drive.google.com/drive/folders/14RCqFVpP_Ubw5K-f_pzEIqg1GdayZHJ9?usp=drive_link)")

        st.write("Top 100 University List with Acronym and Location")
        url = 'https://drive.google.com/file/d/1pKhAaHpV3bvsADYG9VH0N1lQ38YkpVbW/view?usp=sharing'
        if st.button('Download',key=1):
            webbrowser.open_new_tab(url)

        st.write("Original dataset with new columns")
        url1 = 'https://drive.google.com/file/d/1Pv40-AEDL0GyA64IsxdYjZ4fh2lq0zud/view?usp=sharing'
        if st.button('Download', key=2):
            webbrowser.open_new_tab(url1)

        st.write("Authors with All PhD Granting Inst Data")
        url2 = 'https://drive.google.com/file/d/1Pv40-AEDL0GyA64IsxdYjZ4fh2lq0zud/view?usp=sharing'
        if st.button('Download',key=3):
            webbrowser.open_new_tab(url2)

        st.write("Authors with First Employer as Phd Granting Inst Data")
        url3 = 'https://drive.google.com/file/d/1Pv40-AEDL0GyA64IsxdYjZ4fh2lq0zud/view?usp=sharing'
        if st.button('Download',key=4):
            webbrowser.open_new_tab(url3)

        st.write("Author with 2nd or 3rd Employer as PhD Granting Inst Data")
        url4 = 'https://drive.google.com/file/d/1vNZvY6HU_6FXpJQNOL84dFXn1zFUVde4/view?usp=sharing'
        if st.button('Download',key=5):
            webbrowser.open_new_tab(url4)

    with col22:

        st.text_area("Column Descriptions",f.read(),height=1000)
    # pr = df.profile_report()
    # st_profile_report(pr)
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.header("Measurements")
        st.metric(label="Total Found Observations  ", value="2884")
        st.metric(label="Total number of Authors with First Employer as PhD granting institutes", value="2457")
        st.metric(label="Extra people added with hindex>5  ", value="427")
        with st.expander("Update 1"):
            st.write("- Added Acronym column and Location for top100 University data  \n"
                     "- Used previous code to unpack the affiliation column into several columns  \n"
                     "- Matched if the Institutes is in the top100 University data or not  \n"
                     "- Checked if the first Institutes individual worked on is the top100 Uni and the duration is between 4 to 6  \n"
                     "- Separate those author who doesnt fit the criteria with hIndex>5  \n"
                     "- Check if their 2nd or 3rd Employee was in the top100 Uni and the duration is between 4 to 6  \n"
                     "- Add them back to the large dataset with their Phd Granting University column value  \n"
                     "- Created Streamlit app for easy viewing and a repository ")
        st.header("Objectives")
        txt = st.markdown(text)
    with col2:
        # df = 1
        st.header("Top 10 Phd Granitng Universities")
        image = Image.open('top_10_newphdgrantinst.png')
        df = pd.read_csv("top_100_universities.csv")


        st.image(image)
        st.header("List of Top 100 Universities (Popular Acronym and Location manually added)")
        st.dataframe(df)


    # st.divider()
    # st.header("Data")

with tab3:
    with st.expander("See Logic"):
        st.write("Here are some logics:")

    code = '''def hello():
    print("Hello, Streamlit!")'''
    st.code(code, language='python')

# In[4]:






