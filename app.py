import streamlit as st
import joblib
model = joblib.load('spam-ham')
st.tltle('SPAM-HAM CLASSIFIER')
ip = st.text_input('Enter your Message')
op = model.predict([ip])
if st.button('predict):
             st.title(op[0])
                           
