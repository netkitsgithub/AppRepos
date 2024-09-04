import streamlit as st
import pandas as pd


with st.sidebar:
    st.write("Hello World! I am streamlit,")
    st.image("./tt7.png",width=500)


df = pd.read_csv("./平安银行数据.csv")
st.dataframe(df)

st.table(df)


##

column1, column2,column3 = st.columns([1, 2, 1])
with column1:
    name = st.text_input("Please input your name:")
    if name:
        st.write(f"Hello！{name}")

with column2:
    st.number_input("Please input your age:")

with column3:
    st.number_input("Please input your sex")

st.divider()

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
    st.text_input("Please input your name2:")
with tab2:
    st.number_input("Please input your age2:")
with tab3:
    st.number_input("Please input your sex2:")

st.divider()

with st.expander("Sex type"):
    st.radio("Please choose your sex3:", ["male", "female"], index=1)

st.divider()
st.file_uploader("File uploader",type=["csv","png"])

##会话状态交互
if "a" not in st.session_state:
    st.session_state["a"] = 0

clicked = st.button("Click me add 1")
if clicked:
    st.session_state["a"] += 1

st.write(st.session_state["a"])