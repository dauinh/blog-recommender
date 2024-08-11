import streamlit as st


st.set_page_config(
    page_title="Profile",
    page_icon="👤",
)

if 'user_profile' in st.session_state:
    user_profile = st.session_state['user_profile']

    st.title(f"Welcome to your profile")

    # Display preferences
    st.subheader('Your favorite topics:')
    for p in user_profile['topics']:
        st.write(p)

    # Modify preferences
    add = st.text_input('Add to your preferences')
    if add:
        st.info(f"`{add}` has been added to your preferences!")
        st.balloons()
else:
    st.error("You are not logged in!")