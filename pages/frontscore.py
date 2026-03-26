# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:38:36 2026

@author: Mogale
"""
import streamlit as st

st.title("🌍 FrontScore - Cold Front Scoring Model")

st.subheader("Overview")
st.write("""
FrontScore is a continuous 0–1 index to detect and characterise cold-front episodes using single-station meteorological data.
""")

st.subheader("Tools & Techniques")
st.write("""
- Python, Pandas, NumPy  
- Feature engineering on temperature, pressure, wind  
- Regression models and grid optimisation  
- Data cleaning and rolling-window analysis
""")

st.subheader("Key Learnings / Outcomes")
st.write("""
- Built a practical, interpretable metric for frontal intensity  
- Confirmed physical relevance of pressure, temperature, and wind components  
- Learned feature weighting and grid search optimisation  
- Gained experience handling hourly meteorological time-series data
""")

st.subheader("Project Presentation")
st.write("[View PDF on GitHub](https://github.com/mogalezach/Projects-Portfolio/blob/main/frontscore-model.pdf)")