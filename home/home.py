# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 04:44:51 2026

@author: Mogale
"""

import streamlit as st

st.set_page_config(
    page_title="Zacharia Mogale Portfolio",
    layout="wide"
)

st.title("Zacharia Mogale")
st.subheader("Data Scientist | Time Series Analytics")

st.markdown("---")
st.header("Welcome to my Portfolio")
st.write(
    """
    Use the sidebar to navigate between projects.
    Each project page contains:
    - Overview
    - Tools & Techniques
    - Key Learnings / Outcomes
    - Embedded PDF presentation
    """
)
st.info("This portfolio highlights Data Science, Machine Learning, and Time Series projects.")