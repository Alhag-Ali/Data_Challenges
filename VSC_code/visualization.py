import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None

bw = pd.DataFrame(pd.read_csv("./data/bw.csv"))
fw = pd.DataFrame(pd.read_csv("./data/fw.csv"))
lb = pd.DataFrame(pd.read_csv("./data/lb.csv"))
ma = pd.DataFrame(pd.read_csv("./data/ma.csv"))
mi = pd.DataFrame(pd.read_csv("./data/mi.csv"))
om = pd.DataFrame(pd.read_csv("./data/om.csv"))
ts = pd.DataFrame(pd.read_csv("./data/ts.csv"))
cl = pd.DataFrame(pd.read_csv("./data/cl.csv"))


n_rows = st.slider("Choose number of rows to display",
                    min_value=1, max_value=len(cl), step=1)
n_columns = st.multiselect("Select columns to show", cl.columns, default=cl.columns)
st.write(cl[:n_rows][n_columns])

cl_SEX = cl["SEX"].value_counts().reset_index()
st.write(cl_SEX)

cl_SEX.columns = ['SEX', 'number']

# Plotly-Balkendiagramm erstellen
fig = px.bar(cl_SEX, x='SEX', y='number', title="Distribution of Gender", color_discrete_sequence=['#FF5733'])

# Plot in Streamlit anzeigen
st.plotly_chart(fig)

# MA table  
ma_MAORRES_MALE = len(ma[(ma["MAORRES"] == "UNREMARKABLE") & (ma["SEX"] == "M")])
ma_MAORRES_FEMALE = len(ma[(ma["MAORRES"] == "UNREMARKABLE") & (ma["SEX"] == "F")])
ma_MAORRES_dic = {"Sex": ["M", "F"],
                    "Number": [ma_MAORRES_MALE, ma_MAORRES_FEMALE]}
ma_MAORRES_dataFrame = pd.DataFrame(ma_MAORRES_dic)

ma_MAORRES_fig = px.bar(ma_MAORRES_dataFrame, x="Sex", y="Number", title="Unremarkable of Male and famale in ma-table", color_discrete_sequence=['#FF5733'])
st.plotly_chart(ma_MAORRES_fig)

# OM table
# Extract 2 Columns to work with
om_abbreviated = om[["SEX", "OMTESTCD", "OMSTRES"]]
om_SEX_OMTEST_OWBW_MALE = om_abbreviated[(om_abbreviated["SEX"] == "M") & (om_abbreviated["OMTESTCD"] == "OWBW")]
om_SEX_OMTEST_OWBW_FEMALE = om_abbreviated[(om_abbreviated["SEX"] == "F") & (om_abbreviated["OMTESTCD"] == "OWBW")]

# Compute the mean of the Organ weight to Body weight
om_SEX_OMTEST_OWBW_MALE_mean = om_SEX_OMTEST_OWBW_MALE["OMSTRES"].mean()
om_SEX_OMTEST_OWBW_MALE_Female = om_SEX_OMTEST_OWBW_FEMALE["OMSTRES"].mean()

om_DataFrame = {"Sex": ["M", "F"],
                "Mean_of_OWBW": [om_SEX_OMTEST_OWBW_MALE_mean, om_SEX_OMTEST_OWBW_MALE_Female]}

om_SEX_OWBW_DataFrame = pd.DataFrame(om_DataFrame)
st.write(om_SEX_OWBW_DataFrame)
om_SEX_OWBW_fig = px.bar(om_SEX_OWBW_DataFrame, x="Sex", y="Mean_of_OWBW", title="#",
                        color_discrete_sequence=['#FF5733'])
st.plotly_chart(om_SEX_OWBW_fig)

# ts table
lb_LBCAT_GROUP = lb["LBCAT"].value_counts().reset_index()

# Benutzerdefinierte Farbskala erstellen
custom_colors = [(0, "#FFE6D5"), (0.5, "#FF8A66"), (1, "#FF5733")]

lb_LBCAT_GROUP_fig = px.bar(lb_LBCAT_GROUP, x="count", y="LBCAT", 
                            title="Anzahl der getesteten Parameter",
                            labels={"index": "Tested Parameter", "LBCAT": "Counts"},
                            color="LBCAT",  # Setze die Farbe basierend auf den "LBCAT"-Werten
                            color_continuous_scale=custom_colors)
st.plotly_chart(lb_LBCAT_GROUP_fig)


