


import pandas as pd 
import datetime
from pydrive.auth import GoogleAuth

from pydrive.drive import GoogleDrive

from google import auth

from oauth2client.client import GoogleCredentials
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
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

def read_private_file_from_gdrive(
    file_url: str, file_format: str, google_auth: GoogleAuth, **kwargs
) -> Union[pd.DataFrame, Dict, str]:
    """Read private files from Google Drive.
    Parameters
    ----------
    file_url : str
        URL adress to file in Google Drive.
    file_format : str
        File format can be 'csv', 'xlsx', 'parquet', 'json' or 'txt'.
    google_auth: GoogleAuth
        Google Authentication object with access to target account. For more
        information on how to login using Auth2, please check the link below:
        https://docs.iterative.ai/PyDrive2/quickstart/#authentication
    Returns
    -------
    Union[pd.DataFrame, Dict, str].
        The specified object generate from target file.
    """
    drive = GoogleDrive(google_auth)

    # Parsing file URL
    file_id = file_url.split("/")[-2]

    file = drive.CreateFile({"id": file_id})

    content_io_buffer = file.GetContentIOBuffer()

    if file_format == "csv":
        return pd.read_csv(
            StringIO(content_io_buffer.read().decode()), **kwargs
        )

    elif file_format == "xlsx":
        return pd.read_excel(content_io_buffer.read(), **kwargs)

    elif file_format == "parquet":
        byte_stream = content_io_buffer.read()
        return pd.read_parquet(BytesIO(byte_stream), **kwargs)

    elif file_format == "json":
        return json.load(StringIO(content_io_buffer.read().decode()))

    elif file_format == "txt":
        byte_stream = content_io_buffer.read()
        return byte_stream.decode("utf-8", **kwargs)


read_private_file_from_gdrive("https://drive.google.com/file/d/1aVxcutWuwqzCP0fvWbxkBBjJtPy4Wu31/view?usp=drive_link","csv")






# In[4]:

st.title("Stock Prediction")


# today = datetime.date.today()
# lastfive = today - datetime.timedelta(days=23)
#
# day = today.strftime ("%d/%m/%Y")
# five = lastfive.strftime ("%d/%m/%Y")
#
#
#
#
#
#
# st.header("Upload a csv file downloaded from Investing.com")
#
# st.caption("You can Drag and drop the file into the box")
#
# from io import StringIO
#
# stockdata = pd.DataFrame()
#
# file = st.file_uploader("Please choose a csv file")
#
# if file is not None:
#
#     #To read file as bytes:
#
#     bytes_data = file.getvalue()
#
# #     st.write(bytes_data)
#
#     df= pd.read_csv(file)
#     stockdata = df
# #     st.write(df)
#
# # st.write(stockdata)
#
#
# submit = st.button("Submit")
# st.subheader("Green = Abnormal Profit,  Blue = Players detected,     Black = Normal,   Red = Players exiting ")
# if submit:
#     stockdata = stockdata[stockdata['Vol.'].notna()]
#     stockdata["Vol."]=stockdata['Vol.'].replace({'K': '*1e3', 'M': '*1e6', '-':'-1'}, regex=True).map(pd.eval).astype(int)
#     stockdata = stockdata[::-1]
#     stockdata = add_all_ta_features(stockdata, open="Open", high="High", low="Low", close="Price", volume="Vol.", fillna=True)
#     stockdata["VolAvgNDays"] = stockdata["Vol."].rolling(20).mean()
#     stockdata['Change %'] = stockdata['Change %'].str.rstrip('%').astype('float') / 100.0
#     check = stockdata.drop(["Date"],axis=1)
#     st.write(len(check.columns))
#     pred = model1.predict(check)
#     prof = model2.predict(check)
#     stockdata["Prediction"] = pred
#     stockdata["Profit"] = prof
#     stockdata = stockdata[::-1]
#     sts = stockdata[["Date","Price","Prediction","Profit"]]
# #     st.write(stockdata)
#
#
#
#
#
#     def aggrid_interactive_table(df: pd.DataFrame):
#
#         """Creates an st-aggrid interactive table based on a dataframe.
#         Args:
#         df (pd.DataFrame]): Source dataframe
#         Returns:
#         dict: The selected row
#         """
#         options = GridOptionsBuilder.from_dataframe(
#             df, enableRowGroup=True, enableValue=True, enablePivot=True
#         )
#         jscode = JsCode("""
#                     function(params) {
#
#                         if (params.data.Profit === 1) {
#                             return {
#                                 'color': 'white',
#                                 'backgroundColor': 'green'
#                             }
#                         }
#                         if (params.data.Prediction === 0) {
#                             return {
#                                 'color': 'white',
#
#                             }
#                         }
#                     };
#                     """)
#         gridOptions=options.build()
#         gridOptions['getRowStyle'] = jscode
#         options.configure_side_bar()
#         #options.configure_selection("single")
#
#         selection = AgGrid(
#             df,
#             enable_enterprise_modules=True,
#             gridOptions=gridOptions,
#             height=500,
#             width="100%",
#
#
#             theme="alpine",
#             #update_mode=GridUpdateMode.MODEL_CHANGED,
#             allow_unsafe_jscode=True,
#         )
#         return selection
#
#     selection = aggrid_interactive_table(df=sts)
#


