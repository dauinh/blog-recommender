# https://discuss.streamlit.io/t/how-to-add-delete-a-new-row-in-data-editor-in-streamlit/70608
import streamlit as st
import pandas as pd
import requests

try:
    user_id = st.session_state['user_id']
    res = requests.get(url=f"http://127.0.0.1:8000/users/{st.session_state.user_id}").json()
    user_profile = res['user']

    st.title(f"Welcome to your profile, {user_profile['name']}")
    rows = []
    for p in user_profile['preferences']:
        rows.append({'topic': p, 'check': True})

except KeyError:
    st.warning("You are not logged in!")

# Get user preferences
# res = requests.get(url=f"http://127.0.0.1:8000/users/{st.session_state.user_id}").json()
# preferences = res['user']['preferences']
# rows = []
# for p in preferences:
#     rows.append({'topic': p})
#     # rows.append({'topic': p, 'check': True})

# # Save current user info in session state
# st.session_state.df = pd.DataFrame(rows)
# # Display preferences
# st.caption('Your preferences')
# st.table(st.session_state.df)





# Modify preferences
# print('\nsession state\n', st.session_state)
# st.subheader('Make changes to your preferences')

# col1, col2 = st.columns([2, 1], gap='medium')

# with col1:
#     edited_df = st.data_editor(st.session_state.df, use_container_width=True)
# with col2:
#     add = st.button('add')
#     save = st.button('save')

# if add:
#     new_df = pd.DataFrame([{'topic':None,'check':True}])

#     # Add this new_df to the existing st.session_state.df.
#     st.session_state.df = pd.concat([st.session_state.df, new_df], ignore_index=True)
#     st.rerun()  # to rerender the updated value of st.session_state.df

# if save:
#     st.session_state['df'].to_csv('data_temp.csv', index=False)