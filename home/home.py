# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 04:44:51 2026

@author: Mogale
"""

import streamlit as st

st.set_page_config(page_title="Zacharia Mogale Portfolio", layout="wide")

st.title("Zacharia Mogale")
st.subheader("Data Scientist")

st.markdown("---")

st.header("Projects")

st.page_link("pages/1_FrontScore.py", label="🌍 FrontScore")
st.page_link("pages/2_Crypto_TimeSeries.py", label="💰 Crypto Analysis")

import streamlit as st

st.set_page_config(layout="wide")

st.title("FrontScore")

st.write("Climate-based scoring model for cold fronts.")