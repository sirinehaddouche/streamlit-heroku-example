import streamlit as st

st.title('Hello World!')

form = st.form(key='my_form')
text = form.text_input(label='Enter some text')
submit_button = form.form_submit_button(label='Submit')

if submit_button:
    st.subheader('Data')
    st.write({"text": text})
