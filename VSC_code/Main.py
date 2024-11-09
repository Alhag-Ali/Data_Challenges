import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

# bw = pd.DataFrame(pd.read_csv("./data/bw.csv"))
# st.write(bw)

cl = pd.DataFrame(pd.read_csv("./data/bw.csv"))

n_rows = st.slider("Choose number of rows to display",
                   min_value=1, max_value=len(cl), step=1)
n_columns = st.multiselect("Select columns to show", cl.columns, default=cl.columns)
st.write(cl[:n_rows][n_columns])

cl_SEX = cl["SEX"].value_counts().reset_index()
print("cl_SEX", cl_SEX)
st.write(cl_SEX)

cl_SEX.columns = ['SEX', 'number']

# Plotly-Balkendiagramm erstellen
fig = px.bar(cl_SEX, x='SEX', y='number', title="Distribution of the SEX", color_discrete_sequence=['#FF5733'])

# Plot in Streamlit anzeigen
st.plotly_chart(fig)