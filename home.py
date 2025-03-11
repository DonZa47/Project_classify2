from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("การพยากรณ์โรคหัวใจล้มเหลว")
st.header("👨🏽‍⚕️👨🏽‍⚕️ด้วยเทคนิคเหมืองแร่ข้อมูล👨🏽‍⚕️👨🏽‍⚕️")

st.image('./img/H1.jpg')

c1,c2,c3=st.columns(3)
with c1:
    st.wrine('./img/H1.jpg')
with c2:
    st.wrine('./img/H2.Jpg')
with c3:
    st.write("")

dt= pd.read_csv('./data/heart 2.csv')

st.header("ข้อมูลโรคหัวใจ")
st.write(dt.head(10))

count_male = dt.groupby('Sex').size()[1]
count_female = dt.groupby('Sex').size()[0]
dx = [count_male, count_female]
dx2 = pd.DataFrame(dx, index=["Male", "Female"])
st.bar_chart(dx2)