import streamlit as st
from datetime import datetime
import requests
from addorupdate import add_or_update_expense
from analyticss import analytics

API_URL = "http://localhost:8000"

st.title("Expense Tracker")

tab1, tab2 = st.tabs(["Add Expense", "Analytics"])

with tab1:
    add_or_update_expense()
    
with tab2:
    analytics()