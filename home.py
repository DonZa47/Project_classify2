from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("👨🏽‍⚕️👨🏽‍⚕️การพยากรณ์โรคหัวใจล้มเหลวด้วยเทคนิคเหมืองแร่ข้อมูล👨🏽‍⚕️👨🏽‍⚕️")
st.header("👨🏽‍⚕️👨🏽‍⚕️การพยากรณ์โรคหัวใจล้มเหลวด้วยเทคนิคเหมืองแร่ข้อมูล👨🏽‍⚕️👨🏽‍⚕️")

st.image('./img/H1.jpg')

c1,c2,c3=st.columns(3)
with c1:
    st.wrine('./img/H1.jpg')
with c2:
    st.wrine('.')