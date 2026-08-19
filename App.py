import streamlit as st
import pickle
import helper

q1=st.text_input("Question1")
q2=st.text_input("Question2")

with open ('models/q_pair_detection.pkl','rb') as f:
    model=pickle.load(f)

if st.button('Find'):
    q=helper.create_query_point(q1,q2)
    result=model.predict(q)[0]

    if result:
        st.success('Duplicate')
    else:
        st.success('Not Duplicate')

