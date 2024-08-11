import os
import requests
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.set_page_config(
    page_title="Blog Recommender",
    page_icon="📰",
)

st.title("Blog Recommender")

# Prompt user id
with st.popover("Quick 'login'"):
    st.markdown("Hello there 👋")
    id = st.text_input('What is your user id?')
    
    if id and id.isdigit():
        response = requests.get(url=f"{os.environ.get("APP_URL")}/users/{id}")
        res = response.json()
        if "message" not in res:
            st.session_state.user_profile = res["user"]
        else:
            st.error("User not found")


# Recommend articles
if 'user_profile' in st.session_state:
    id = st.session_state['user_profile']['user_id']
    st.header('Read your favorite article right here!')

    if st.button('Get recommendations'):
        response = requests.get(url=f"{os.environ.get("APP_URL")}/users/{id}/recommendations").json()
        if response:
            for r in response:
                article = r["blog"]
                st.image(article["blog_img"])
                st.subheader(f"[{article["blog_title"]}]({article["blog_link"]})")
                st.caption(article["topic"])
                st.write(article["blog_content"])