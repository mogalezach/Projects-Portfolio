# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:31:39 2026

@author: Mogale
"""

import streamlit as st

st.title("🏠 Resale Value Prediction")

st.subheader("Overview")
st.write("""
Predicting resale property values using machine learning in R.
""")

st.subheader("Tools & Techniques")
st.write("""
- R, caret, regression trees, LASSO, Ridge, Elastic Net  
- KNN imputation and feature engineering  
- Train/test split and k-fold cross-validation  
- Model comparison using MAE
""")

st.subheader("Key Learnings / Outcomes")
st.write("""
- Handled missing values with regression trees and KNN  
- Built multiple ML models and compared predictive accuracy  
- Learned hyperparameter tuning and cross-validation  
- Developed model interpretability skills
""")

st.subheader("Project Presentation")
st.write("[View PDF on GitHub](https://github.com/mogalezach/Projects-Portfolio/blob/main/resale-prediction.pdf)")