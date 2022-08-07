import osmnx as ox
import plotly.offline as pyo
import streamlit as st
from io import BytesIO
import requests

from PIL import Image

st.set_page_config(
    page_title="Home",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("<h1 style='text-align: center; color: #4169e1;margin-top:-50px;'>OMDENA-DRIQ HEALTH</h1>", unsafe_allow_html=True)
st.write("")
st.write("")
st.subheader('IMPROVING THE QUALITY OF LIFE FOR SENIORS IN NURSING HOMES')
st.markdown('<h5>PROBELM STATEMENT:</h5>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns([4,0.1,0.2,2.5])

with col1:
    
    st.markdown("""
    Without monitoring technology in nursing homes, the staff cannot determine the status of the seniors and whether \
    they have been lying down with a wet diaper for hours. Consequently, this issue impacts their quality of life, \
    placing them at significant risk for skin breakdown and life-threatening urinary tract infections. Impact-driven \
    startup Driq Health´s non-contact sensor monitoring can solve this by allowing real-time notifications for timely \
    diaper changes as well as providing mobility alerts.
    
    Goals of this Project comprises of :
    
    - Develop a more accurate wet vs. dry state that reduces the current false positive rate, which is 20%. \
    - Help prevent skin breakdown by preventing seniors from chronically lying in the same position in bed by detecting resident positional changes and issuing alerts.

    Scope of the Project involves :

    - work on the EDA to provide different visualizations and feedback on the data quality and quantity. \
    - Do the proper data processing, cleaning, and feature selection. \
    - Incorporate the temperature picked up by the sensor to improve the currently used algorithm. \
    - Train a machine learning model to accurately distinguish between the wet vs. dry state with a false positive rate of less than 5%. \
    - Analyze the relative strength of the twin antenna signal to decide the resident’s position on the bed. \
    - Decide whether it is optimal to integrate the model using an edge approach managed on the device or on the cloud. \
    
    """,  unsafe_allow_html=True)
    
    
