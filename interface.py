import json
import requests
import streamlit as st
import pandas as pd

def add_preferences():
    with st.form("preferences", clear_on_submit=True):
        input = st.text_input("Add more topic")
        submitted = st.form_submit_button("Submit")

        if submitted:
            if not input:
                st.write("Field cannot be empty! Try again!")
            else:
                input = input.strip()
                if input not in preferences:
                    st.write(f"'{input}' has been added to your preferences")
                    return input
                else:
                    st.write("Duplicate preference! Try again!")

st.title("Read your favorite blog article right here!")

preferences = ["technology", "world leaders"]

st.subheader("Your favorite topics")
for p in preferences:
    st.write(p)

add_preferences()