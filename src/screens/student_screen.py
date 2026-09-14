import streamlit as st
from src.ui.base_layout import style_base_layout, style_background_dashboard

def student_screen():
    style_base_layout()
    style_background_dashboard()
    st.header('Student Screen')