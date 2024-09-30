import streamlit as st

st.header('st.button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

if st.button("Reset", type="primary"):
    st.write("Reset button was clicked!")
