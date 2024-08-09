import requests

import streamlit as st


if "user_profile" in st.session_state:
    user_profile = st.session_state["user_profile"]
    id = user_profile["id"]
    history = requests.get(
            url=f"http://127.0.0.1:8000/users/{id}/history"
        ).json()

    st.title("Your blog history")

    for h in history:
        article = h['blog']
        st.subheader(article["title"])
        st.caption(article["category"])

else:
    st.error("You are not logged in!")
