import os
import requests
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


if "user_profile" in st.session_state:
    user_profile = st.session_state["user_profile"]
    id = user_profile["id"]
    history = requests.get(
            url=f"{os.environ.get("APP_URL")}/users/{id}/history"
        ).json()

    st.title("Your blog history")

    for h in history:
        article = h['blog']
        st.subheader(article["title"])
        st.caption(article["category"])

else:
    st.error("You are not logged in!")
