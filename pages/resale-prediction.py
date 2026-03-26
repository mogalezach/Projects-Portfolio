# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:31:39 2026

@author: Mogale
"""

# pages/3_Resale_Prediction.py
import streamlit as st
import streamlit.components.v1 as components

st.title("🏠 Resale Value Prediction")

st.subheader("Overview")
st.write("""
Predictive models using machine learning in R to estimate resale property values.  
Focus on handling non-linear relationships and imputation of missing data.
""")

st.subheader("Tools & Techniques")
st.write("""
- R (caret, glmnet, rpart)  
- Regression, Ridge, LASSO, Elastic Net  
- Regression trees, SVR, KNN, Neural Networks  
- K-fold cross-validation and hyperparameter tuning
""")

st.subheader("Key Learnings / Outcomes")
st.write("""
- Practiced full ML workflow from data cleaning to model evaluation  
- Learned advanced imputation techniques (KNN, regression tree)  
- Compared multiple models using MAE and overfitting diagnostics  
- Selected best-performing model and interpreted feature importance  
- Gained insight into practical real-estate prediction modeling
""")

st.subheader("Project Presentation")
pdf_url = "https://raw.githubusercontent.com/mogalezach/Projects-Portfolio/main/resale-prediction.pdf"
components.iframe(pdf_url, height=600)
