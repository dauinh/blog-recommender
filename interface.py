# https://discuss.streamlit.io/t/how-to-add-delete-a-new-row-in-data-editor-in-streamlit/70608
import streamlit as st
import pandas as pd


list = [{'name': 'Love', 'check': True},
        {'name': 'Smells Like Teen Spirit', 'check': True},
        {'name': 'Lithium', 'check': True},
        {'name': 'All Apologies', 'check': True},
        {'name': 'Stay Away', 'check': True}]


# Create a variable to hold the dataframe. Initialize it with the given list.
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(list)


st.title('Blog Recommender System')

st.subheader('Read your favorite article right here!')

if st.button('Get recommendations'):
    st.write('Enjoy your read')


st.subheader('Make changes to your preferences')

col1, col2 = st.columns([2, 1], gap='medium')

with col1:
    edited_df = st.data_editor(st.session_state.df, use_container_width=True)
with col2:
    add = st.button('add')
    save = st.button('save')

if add:
    new_df = pd.DataFrame([{'name':None,'check':None}])

    # Add this new_df to the existing st.session_state.df.
    st.session_state.df = pd.concat([st.session_state.df, new_df], ignore_index=True)
    st.rerun()  # to rerender the updated value of st.session_state.df

if save:
    st.session_state['df'].to_csv('data_temp.csv', index=False)