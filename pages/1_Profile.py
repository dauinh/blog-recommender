import os
import requests
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.set_page_config(
    page_title="Profile",
    page_icon="👤",
)

@st.dialog("Notification")
def noti():
    st.balloons()
    st.info(f"`{add}` has been added to your preferences!\nLog in again to see the difference")
    if st.button("Okay"):
        st.switch_page("Home.py")
        

if 'user_profile' in st.session_state:
    user_profile = st.session_state['user_profile']
    id = user_profile["user_id"]
    preferences = user_profile["topics"]

    st.title(f"Welcome to your profile")

    # Display preferences
    st.subheader('Your favorite topics:')
    for p in user_profile['topics']:
        st.write(p)

    # Modify preferences
    add = st.text_input("Add to your preferences")
    if add:
        if add in preferences:
            st.error(f"`{add}` already exists!")
        else:
            response = requests.put(
                url=f"{os.environ.get("APP_URL")}/users/{id}/?preference={add}"
            )
            if response:
                noti()
            else:
                st.error("An error has occurred. Try again!")
else:
    st.error("You are not logged in!")
