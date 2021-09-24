import streamlit as st
import sklearn
import pickle
st.title("First APP")
st.text("enter first number")
classes=['setosa','virsicolor','virginica']
a=st.number_input("enter first number",0.0)
b=st.number_input("enter second number",0.0)
c=st.number_input("enter third number",0.0)
d=st.number_input("enter fouth number",0.0)
model=pickle.load(open('irismodel.pkl','rb'))
p=model.predict([[a,b,c,d]])
st.write("class is",classes[p[0]])
