import csv
import streamlit as st
import streamlit.components.v1 as components


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

filename = "yt-videos.csv"

st.title("農業ユーチューブ")

with open(filename, "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        st.subheader(row[0])
        st.video(row[2])
