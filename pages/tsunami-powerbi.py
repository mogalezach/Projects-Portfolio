# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:33:49 2026

@author: Mogale
"""

# pages/5_Tsunami_PowerBI.py
import streamlit as st
import streamlit.components.v1 as components

st.title("🌊 Tsunami Damage Analysis (Power BI)")

st.subheader("Overview")
st.write("""
Interactive Power BI report analyzing historical tsunami data to understand factors 
influencing damage (deaths, houses destroyed, total cost) across geographies.
""")

st.subheader("Tools & Techniques")
st.write("""
- Power BI (interactive dashboards)  
- Excel for pre-processing and missing value handling  
- Geo-coded visualization of tsunami events  
- Visual storytelling and report presentation
""")

st.subheader("Key Learnings / Outcomes")
st.write("""
- Learned to create interactive dashboards for large geospatial datasets  
- Applied data cleaning and transformation techniques  
- Explored relationships between event characteristics and damage  
- Practiced effective visual storytelling in data reports  
- Gained experience combining technical analysis with clear communication
""")

st.subheader("Project Presentation")
pdf_url = "https://raw.githubusercontent.com/mogalezach/Projects-Portfolio/main/tsunami-powerbi-report.pdf"
components.iframe(pdf_url, height=600)
