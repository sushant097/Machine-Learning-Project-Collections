import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

page_select = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page_select == "Predict":
    show_predict_page()
else:
    show_explore_page()