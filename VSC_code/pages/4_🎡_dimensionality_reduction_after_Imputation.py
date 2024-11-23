import pandas as pd
import streamlit as st
import plotly.express as px

cl = pd.DataFrame(pd.read_csv("./data/cl.csv"))

cl_abbreviated = cl.drop(['CLLOC', 'CLREASND', 'CLSEV', 'CLSTAT'], axis = 1, inplace = False)
cl_CLTPTNUM = cl_abbreviated["CLTPTNUM"].value_counts().reset_index()

# Creating a user definite color scala
custom_colors = ["#FFB199", "#FF8A66", "#FF7251", "#FF5733", "#E04E2E", "#CC462A"]

cl_abbreviated_preImputation_fig = px.bar(cl_CLTPTNUM, x="CLTPTNUM", y="count", 
                            title="Distribution of CLTPTNUM before the Imputation",
                            labels={"index": "Tested Parameter", "LBCAT": "Counts"},
                            color_discrete_sequence=custom_colors)
st.plotly_chart(cl_abbreviated_preImputation_fig)

cl_CLTPTNUM = cl_abbreviated["CLTPTNUM"].value_counts()
# Getting the probability of each item in the column.
my_dic = {}

# to select a random numer with the probabilities for CLTPTNUM.
import random
def choice_number_CL():
    keys = [6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
    selected_number = random.choices(keys, cum_weights=(0.002734553030796276, 0.00283221563903900,
                                                        0.025587603359593723, 0.18770753304251578,
                                                        0.389348264860993550, 0.39178983006706164), k=1)
    #print(selected_number)
    return selected_number[0]

# the keys are 1, 2, 3, 4, 5 and 6
count = 0 
for CLTP in cl_CLTPTNUM:
    count += 1
    cl_percent = CLTP / cl_CLTPTNUM.sum()
    my_dic.update({count:cl_percent})
my_dic

cl_abbreviated["CLTPTNUM"] = cl_abbreviated["CLTPTNUM"].apply(lambda x: choice_number_CL() if pd.isna(x) else x)
cl_CLTPTNUM_imputation = cl_abbreviated["CLTPTNUM"].value_counts().reset_index()
print("---------------------------",cl_CLTPTNUM_imputation)
# Creating a user definite color scala
custom_colors = ["#FFB199", "#FF8A66", "#FF7251", "#FF5733", "#E04E2E", "#CC462A"]

cl_abbreviated_fig = px.bar(cl_CLTPTNUM_imputation, x="CLTPTNUM", y="count", 
                            title="Distribution of CLTPTNUM after the Imputation",
                            labels={"CLTPTNUM": "Tested Parameter", "count": "Counts"},
                            #color="CLTPTNUM",  # Setze die Farbe basierend auf den "LBCAT"-Werten
                            color_discrete_sequence=custom_colors)
st.plotly_chart(cl_abbreviated_fig)

st.image("./data/cl_2D.JPG", caption="Dimensionality reduction 2D after Imputation")
st.image("./data/cl_sex.JPG", caption="Dimensionality reduction 2D after Imputation for just a feature")