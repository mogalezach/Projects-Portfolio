# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:38:36 2026

@author: Mogale
"""
# pages/1_FrontScore.py
import streamlit as st
import streamlit.components.v1 as components

st.title("🌍 FrontScore - Cold Front Scoring Model")

st.subheader("Overview")
st.write("""
FrontScore is a continuous 0–1 index designed to detect and characterise cold-front episodes 
using single-station meteorological data from remote Southern Ocean stations.
""")

st.subheader("Tools & Techniques")
st.write("""
- Python, Pandas, NumPy  
- Feature engineering on temperature, pressure, and wind data  
- Regression models and grid optimisation  
- Rolling-window analysis and data cleaning
""")

st.subheader("Key Learnings / Outcomes")
st.write("""
- Developed an interpretable index for frontal intensity  
- Confirmed physical relevance of pressure, temperature, and wind components  
- Practiced feature weighting and model optimisation  
- Gained experience handling hourly meteorological time-series
""")

st.subheader("Project Presentation")
pdf_url = "https://raw.githubusercontent.com/mogalezach/Projects-Portfolio/main/frontscore-model.pdf"
components.iframe(pdf_url, height=600)
