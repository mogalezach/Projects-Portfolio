# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:33:01 2026

@author: Mogale
"""

import streamlit as st

st.title("🚀 Asteroid Classification - Binary Classification")

st.subheader("Overview")
st.write("""
Binary classification problem to predict asteroid types using 4 ML models + ensemble.
""")

st.subheader("Tools & Techniques")
st.write("""
- Python, Scikit-learn  
- Train/test split (80:20), feature engineering  
- Logistic regression, random forest, SVM, ensemble methods  
- Optimal cut-off calculation and feature importance
""")

st.subheader("Key Learnings / Outcomes")
st.write("""
- Learned feature engineering to enhance predictive performance  
- Built ensemble model for classification improvement  
- Evaluated overfitting, underfitting, and model variance  
- Identified top 5 features influencing classification
""")

st.subheader("Project Presentation")
st.write("[View PDF on GitHub](https://github.com/mogalezach/Projects-Portfolio/blob/main/asteroid-classification.pdf)")