# https://discuss.streamlit.io/t/how-to-add-delete-a-new-row-in-data-editor-in-streamlit/70608
import streamlit as st
import pandas as pd
import requests


st.title('Blog Recommender System')


# Prompt user id
st.subheader('First, who are you?')
id = st.selectbox('Choose your id', [1, 2])

# Get user preferences
res = requests.get(url=f"http://127.0.0.1:8000/users/{id}").json()
preferences = res['user']['preferences']
rows = []
for p in preferences:
    rows.append({'topic': p})
    # rows.append({'topic': p, 'check': True})

# Save current user preferences in session state
st.session_state.df = pd.DataFrame(rows)
# Display preferences
st.caption('Your preferences')
st.table(st.session_state.df)


# Recommend articles
st.subheader('Read your favorite article right here!')

if st.button('Get recommendations'):
    res = requests.get(url=f"http://127.0.0.1:8000/users/{id}/recommendations").json()
    print('\ncurrent artilces\n', res)
    for r in res:
        article = r['blog']
        st.write(article['title'])


# Modify preferences
print('\nsession state\n', st.session_state)
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