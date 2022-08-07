from pathlib import Path
import pandas as pd
import numpy as np
import streamlit as st
import plotly_express as px
import chart_studio.plotly as py

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
)

PAGE_TITLE = "Exploratory Data Analysis"
st.sidebar.header("Visualizations")

st.markdown("<h2 style='text-align: center; color: #4169e1;margin-top:-50px;font-weight:bold'>OMDENA-DRIQ HEALTH</h2>", unsafe_allow_html=True)
