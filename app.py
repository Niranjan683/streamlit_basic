import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hello streamlit")

##display a simple text

st.write("This is a Simple Text")

df = pd.DataFrame({
    'first_col':[1,2,3,4,5],
    'second_col':[10,20,30,40,50]
})

# Displaying the data frame 

st.write(" Here is the DataFrame " )
st.write(df)

# Creating a line Chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['A','B','C']
)
st.line_chart(chart_data)