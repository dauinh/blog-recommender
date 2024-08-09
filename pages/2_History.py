import streamlit as st


if "user_profile" in st.session_state:
    user_profile = st.session_state["user_profile"]

    st.title("Your blog history")

    for p in user_profile["history"]:
        st.write(p)

else:
    st.error("You are not logged in!")
