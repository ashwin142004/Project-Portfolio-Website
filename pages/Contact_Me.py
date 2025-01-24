import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="contact_form"):
    user_email = st.text_input("Email")
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject: New message from {user_email}

from: {user_email}
{raw_message}
"""
    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        st.success("Thank you for your message! I will get back to you soon.")
        send_email(message)
