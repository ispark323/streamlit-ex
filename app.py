import csv
import time
import streamlit as st


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

filename = "yt-videos.csv"

st.title("農業ユーチューブ")

with st.spinner("Please wait..."):
    time.sleep(2)

with open(filename, "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        st.video(row[2])
        st.subheader(row[0])
        st.markdown("""---""")
