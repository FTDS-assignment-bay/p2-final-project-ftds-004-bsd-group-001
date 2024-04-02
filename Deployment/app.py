import streamlit as st
import matplotlib as plt
import eda
import predict

#setting page configuration
navigation = st.sidebar.selectbox("Select Page", 
                                  options=['EDA','Predict'])

st.sidebar.write('# About : Apart Helper')
st.sidebar.write('''
This page is created to help customer for choose the best apartment
                 ''')
if navigation =='EDA':
     eda.run()
else:
     predict.run()