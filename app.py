import imghdr
import streamlit as st


st.title("File Upload")

file_uploaded = st.file_uploader("Choose a file")

if file_uploaded is not None:
    st.image(file_uploaded, use_column_width=True)


st.title("Upload Picture")

img = st.camera_input("Upload an image")

if img:
    st.image(img)