import streamlit as st

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.title("肥料計算")

st.text("肥料袋のキロ数から肥料成分量が計算されます。")


form = st.form(key='calc-form')

amount = form.number_input("肥料量（kg）: ", min_value=0, value=20, format="%d", step=1)
n = form.number_input("チッソ割合: ", min_value=0, format="%d", step=1)
p = form.number_input("リン割合: ", min_value=0, format="%d", step=1)
k = form.number_input("カリ割合: ", min_value=0, format="%d", step=1)

submit = form.form_submit_button('計算')

n_calc = amount / 100 * n
p_calc = amount / 100 * p
k_calc = amount / 100 * k

n_format = "{:.1f}".format(n_calc)
p_format = "{:.1f}".format(p_calc)
k_format = "{:.1f}".format(k_calc)

if submit:
    st.write(f"チッソ (N) = {n_format} kg")
    st.write(f"リン (P) = {p_format} kg")
    st.write(f"カリ (K) = {k_format} kg")


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)