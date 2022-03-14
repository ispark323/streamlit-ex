import streamlit as st
import streamlit.components.v1 as components

st.subheader("【伝説】幻の十文字大根、収穫してみた！")
st.video('https://youtu.be/aaFhoLlEkIQ') 

components.html(
    """
    <iframe width="560" height="315" src="https://www.youtube.com/embed/aaFhoLlEkIQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    """,
    height=315,
)
