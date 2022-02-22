import imghdr
import streamlit as st

st.title("Upload Picture")

img = st.camera_input("Upload an image")

if img:
    st.image(img)