#making changes

import streamlit as st
import pandas as pd

df = pd.read_csv('download.csv')

st.dataframe(df)


st.line_chart(data=df, x= 'firstDowns', y='fourthDowns')