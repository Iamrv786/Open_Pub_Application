import streamlit as st
import os
import pandas as pd
import numpy as np
st.markdown("""
    <style>
        body {
            background-image: url("https://cdn.dnaindia.com/sites/default/files/styles/full/public/2017/01/29/543336-raees-srk.png");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background-color: rgba(255, 255, 255, 0.1);
        }
    </style>
""", unsafe_allow_html=True)
# Page Title
# Set page title color
st.markdown(
    """
    <style>
    .title {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Page title
st.markdown("<h1 style='text-align: Right;color:brown''>&nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp Raees Open Pub Application </h1>", unsafe_allow_html=True)

#st.dataframe(pubs_df.head())
# absolute path to this file
st.markdown("<h4 style='text-align: Center;color:black''> &nbsp &nbsp  &nbsp   &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp  &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp [Find Pubs near you and their location]  </h3>",unsafe_allow_html=True)
