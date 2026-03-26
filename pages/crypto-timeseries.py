# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:39:09 2026

@author: Mogale
"""

# pages/2_Crypto_TimeSeries.py
import streamlit as st
import streamlit.components.v1 as components

st.title("💰 Crypto Time Series Analysis")

st.subheader("Overview")
st.write("""
Analyzed daily cryptocurrency closing prices in USD.  
Focused on log returns, volatility analysis, and forecasting using econometric models.
""")

st.subheader("Tools & Techniques")
st.write("""
- Python, Pandas, NumPy, Matplotlib  
- Time series plotting and log return transformation  
- Skewness, kurtosis, ACF plots, ARCH LM tests  
- ARIMA/GARCH modeling and forecast evaluation
""")

st.subheader("Key Learnings / Outcomes")
st.write("""
- Learned to transform and visualize financial time series  
- Practiced statistical testing (mean, variance, autocorrelation)  
- Built ARIMA/GARCH models for cryptocurrency returns  
- Interpreted model outputs and forecast reliability  
- Highlighted implications for fintech risk assessment
""")

st.subheader("Project Presentation")
pdf_url = "https://raw.githubusercontent.com/mogalezach/Projects-Portfolio/main/crypto-time-series.pdf"
components.iframe(pdf_url, height=600)
