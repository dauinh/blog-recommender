import streamlit as st
import pandas as pd
import requests

try:
    user_id = st.session_state['user_id']
    res = requests.get(url=f"http://127.0.0.1:8000/users/{st.session_state.user_id}").json()
    st.session_state.user_profile = res['user']
except KeyError or TypeError:
    st.error("You are not logged in!")


if 'user_profile' in st.session_state:
    user_profile = st.session_state['user_profile']

    st.title(f"Welcome to your profile, `{user_profile['name']}`")

    # Display preferences
    st.subheader('Your favorite topics:')
    for p in user_profile['preferences']:
        st.write(p)

    # Modify preferences
    add = st.text_input('Add to your preferences')
    if add:
        st.info(f"`{add}` has been added to your preferences!")
        st.balloons()