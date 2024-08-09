import requests

import streamlit as st

st.set_page_config(
    page_title="Blog Recommender",
    page_icon="📰",
)

st.title("Blog Recommender")

with st.popover("Quick 'login'"):
    st.markdown("Hello there 👋")
    id = st.text_input('What is your user id?')
    st.session_state.user_id = id

if st.session_state.user_id:
    # Recommend articles
    st.subheader('Read your favorite article right here!')

    if st.button('Get recommendations'):
        res = requests.get(url=f"http://127.0.0.1:8000/users/{id}/recommendations").json()
        print('\ncurrent artilces\n', res)
        for r in res:
            article = r['blog']
            st.write(article['title'])