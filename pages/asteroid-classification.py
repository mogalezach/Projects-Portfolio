# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:33:01 2026

@author: Mogale
"""

# pages/4_Asteroid_Classification.py
import streamlit as st
import streamlit.components.v1 as components

st.title("🚀 Asteroid Binary Classification")

st.subheader("Overview")
st.write("""
Performed binary classification on asteroid datasets using four machine learning models 
plus an ensemble to predict target classes.
""")

st.subheader("Tools & Techniques")
st.write("""
- Python, Pandas, scikit-learn  
- Train/test split (80:20), feature engineering  
- Logistic Regression, Decision Tree, Random Forest, SVM  
- Ensemble model and feature importance analysis
""")

st.subheader("Key Learnings / Outcomes")
st.write("""
- Built and compared multiple ML models for classification tasks  
- Learned to handle missing values and feature engineering  
- Evaluated models for overfitting, underfitting, and high variance  
- Determined optimal cut-off for classification decisions  
- Identified top 5 most important features for prediction
""")

st.subheader("Project Presentation")
pdf_url = "https://raw.githubusercontent.com/mogalezach/Projects-Portfolio/main/asteroid-classification.pdf"
components.iframe(pdf_url, height=600)
