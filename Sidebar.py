import streamlit as st

from app import main
from home import home
from login import login

# Sidebar content
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Login", "Main"])

# Main content based on sidebar selection
st.title("Credit Card Fraud Detection Model")

if page == "Home":
    home()
elif page == "Login":
    login()
elif page == "Main":
    main()
