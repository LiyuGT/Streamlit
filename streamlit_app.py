import streamlit as st
st.write("Hello World")
st.write("Welcome to Liyu's world")

x = st.text_input("What's your name?")
st.write(f"Oh, Hi {x}!")
is_clicked = st.button("Send")
