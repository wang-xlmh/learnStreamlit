import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
    'What are your favourite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)

st.write('You selected:', options)
