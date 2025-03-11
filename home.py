from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("👨🏽‍⚕️👨🏽‍⚕️👨🏽‍⚕️การพยากรณ์โรคหัวใจล้มเหลวด้วยเทคนิคเหมืองแร่ข้อมูล👨🏽‍⚕️👨🏽‍⚕️")
st.header("👨🏽‍⚕️👨🏽‍⚕️👨🏽‍⚕️การพยากรณ์โรคหัวใจล้มเหลวด้วยเทคนิคเหมืองแร่ข้อมูล👨🏽‍⚕️👨🏽‍⚕️")

st.image('./img/pic.jpg')
st.subheader("ธนดล จันทวงค์")
col1,col2,col3 = st.columns(3)
with col1:
    st.header("tuilpa")
    st.image("./img/H1.jpg")

with col2:
    st.header("Helianthus annuus")
    st.image("./img/H2.jpg")

with col3:
    st.header("Myostis")
    st.image("./img/H3.jpg")
    