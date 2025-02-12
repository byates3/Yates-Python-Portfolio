import pandas as pd
import streamlit as st

# to run this streamlit app, use:
# streamlit run ./main.py

st.title("Penguins of the World")
st.markdown("This app contains data on 3 species of penguins on 3 islands. \
            Data includes the length and depth of bills in mm, flipper length \
            in mm, body mass in g, sex, and year the datapoint was collected. \
            Users can filter through the data either by species or by island.")

st.subheader("Data for all penguins on all islands:")

df = pd.read_csv("data/penguins.csv")
st.dataframe(df)

st.subheader("Filtering the data")

st.markdown("By species")

species = st.selectbox("Select a species.", df["species"].unique())
filtered_df = df[df["species"] == species]
st.write(f"{species} penguins")
st.dataframe(filtered_df)

st.markdown("By island")

island = st.selectbox("Select an island.", df["island"].unique())
filtered_df1 = df[df["island"] == island]
st.write(f"Penguins on {island} island")
st.dataframe(filtered_df1)