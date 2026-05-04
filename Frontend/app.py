import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"

st.title("Expense Tracker")

tab1, tab2 = st.tabs(["Add Expense", "Analytics"])

with tab1:
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1), label_visibility="collapsed")
    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code ==200:
        existing_expenses = response.json()
        st.write(existing_expenses)
    else:
        st.write("failed to retrive expenses")
        existing_expenses = []
    with st.form(key="expense_form"):
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader(f"Amount")
        with col2:
            st.subheader(f"Category")
        with col3:
            st.subheader(f"Notes")
        categories = ["Rent", "Shopping", "Food", "Transport", "Entertainment", "Utilities", "Other"]
        expenses = []
        for i in range(5):
            
            if i < len(existing_expenses):
                amount = existing_expenses[i]["amount"]
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Food"
                notes = ""
            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input =st.number_input(label="Amount", min_value=0.0, step=1.0, value=amount, key=f"amount_{i}_{selected_date}", label_visibility="collapsed")
            with col2:
                category_input =st.selectbox(label="Category", options=categories, key=f"category_{i}_{selected_date}", index=categories.index(category), label_visibility="collapsed")
            with col3:
                notes_input =st.text_input(label="Notes", value=notes, key=f"notes_{i}_{selected_date}", label_visibility="collapsed")
            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })
        submit_button = st.form_submit_button()
        if submit_button:
            filtered_expenses = [{**expense, 'expense_date': str(selected_date)} for expense in expenses if expense['amount'] > 0]
            response = requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)
            if response.status_code == 200:
                st.success("Expenses saved successfully!")
            else:
                st.error("Failed to save expenses.")