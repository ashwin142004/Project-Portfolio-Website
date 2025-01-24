import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ashwin N Mysore", page_icon=":smiley:", layout="wide", initial_sidebar_state="auto")

col1, col2 = st.columns(2)

with col1:
    st.image("D:\\Project-Portfolio-Website\\images\\photo.png", width=400)

with col2:
    st.title("Ashwin N Mysore")
    content = """
    Hi, I am Ashwin! I am an Engineering student at BNM Institute of Technology. I am currently in my 3rd year of study. 
    I am passionate about Data Science and Machine Learning. I am also interested in Web Development. I am currently learning and working on projects in these fields. 
    I an glad to share my projects with you thrugh this portfolio that I have created. 
    """
    st.info(content)

content2 = """
Below you can find some of the apps i have built. Feel free to explore them!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pd.read_csv("D:\\Project-Portfolio-Website\\data.csv", sep = ";")
with col3:
    for index, row in df[:10].iterrows():
        st.header( row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])