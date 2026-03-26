# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:39:09 2026

@author: Mogale
"""

import streamlit as st

st.title("💰 Cryptocurrency Time Series Analysis")

st.subheader("Overview")
st.write("""
Analyzed daily cryptocurrency closing prices to extract insights on volatility and time-series behaviour.
""")

st.subheader("Tools & Techniques")
st.write("""
- Python, Pandas, Matplotlib, Statsmodels  
- Log returns transformation, skewness & kurtosis analysis  
- Autocorrelation (ACF) and ARCH tests  
- GARCH modelling with skewed Student-t innovations
""")

st.subheader("Key Learnings / Outcomes")
st.write("""
- Gained expertise in financial time-series preprocessing  
- Learned to identify volatility clustering and ARCH effects  
- Practiced building predictive models for cryptocurrency  
- Enhanced skills for fintech-focused data analysis
""")

st.subheader("Project Presentation")
st.write("[View PDF on GitHub](https://github.com/mogalezach/Projects-Portfolio/blob/main/crypto-time-series.pdf)")