import os
import requests
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.set_page_config(
    page_title="Profile",
    page_icon="📁",
)


if "user_profile" in st.session_state:
    user_profile = st.session_state["user_profile"]
    id = user_profile["user_id"]
    response = requests.get(
            url=f"{os.environ.get("APP_URL")}/users/{id}/history"
        ).json()
    st.title("Your blog history")

    if response:
        for r in response:
            article = r["blog"]
            st.image(article["blog_img"])
            st.subheader(f"[{article["blog_title"]}]({article["blog_link"]})")
            st.caption(article["topic"])
            st.write(article["blog_content"])
else:
    st.error("You are not logged in!")
