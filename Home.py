import requests

import streamlit as st

st.set_page_config(
    page_title="Blog Recommender",
    page_icon="📰",
)

st.title("Blog Recommender")

# Prompt user id
with st.popover("Quick 'login'"):
    st.markdown("Hello there 👋")
    id = st.text_input('What is your user id?')
    
    response = requests.get(url=f"http://127.0.0.1:8000/users/{id}")
    if response.status_code == 200:
        st.session_state.user_id = id
    else:
        st.error("User not found")


# Recommend articles
if st.session_state.user_id:
    st.header('Read your favorite article right here!')

    if st.button('Get recommendations'):
        res = requests.get(url=f"http://127.0.0.1:8000/users/{id}/recommendations").json()
        print('\ncurrent artilces\n', res)
        for r in res:
            article = r['blog']
            st.subheader(article['title'])