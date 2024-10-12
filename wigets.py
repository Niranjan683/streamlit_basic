import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter Yourr Name : ")
age= st.slider("Select your age:",0,100,25)
st.write(f"Your age is {age}")

options=['Python','Java','C',"Rust"]
choice=st.selectbox("Choose Your programming language :",options)
st.write(f"Successfully you've chosen {choice}")

if name:
    st.write (f" Hello, {name}")
st.write("The DataFrame :")
df=pd.DataFrame({
    'Name':['Logan','Deadpool','x-23','Nicepool'],
    'Place':['TamilNadu','Andra','Kerala','Karnataka'],
})
df.to_csv('sampledata.csv ')
st.write(df)

upload_file = st.file_uploader("Choose a your file ",type=['csv','pdf'])

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)