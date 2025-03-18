import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Streamlit app header
st.header("Portfolio Update 2 - Beau Yates - Mutant Moneyball Data Manipulation and Visualization")
st.divider()

# A description of the aoo and its goals
st.write("This app uses data from the mutant_moneyball.csv dataset. This data will be tidied up and visualized through bar plots and scatter plots.")
st.divider()

# Text introducing the original messy dataset as taken from Canvas
st.subheader("The Original Dataset")
st.write("The following table shows the orignal data as taken from Canvas. This includes missing data.")

#_________________________________________________________________
# Import the Mutant Moneyball dataset
df = pd.read_csv("mutant_moneyball.csv")

# ----Melt the dataframe----
# Original data columns are brought under the 'Value of Issues by Seller column
# with each value being brought under the new 'Value' column
df_melted = pd.melt(df,
            id_vars = ["Member"],
            value_vars = ["TotalValue60s_heritage","TotalValue70s_heritage","TotalValue80s_heritage","TotalValue90s_heritage",\
                    "TotalValue60s_ebay","TotalValue70s_ebay","TotalValue80s_ebay","TotalValue90s_ebay",\
                    "TotalValue60s_wiz","TotalValue70s_wiz","TotalValue80s_wiz","TotalValue90s_wiz",\
                    "TotalValue60s_oStreet","TotalValue70s_oStreet","TotalValue80s_oStreet","TotalValue90s_oStreet"],
            var_name = "Value of Issues by Seller",
            value_name = "Value")

# Display the melted dataset in Streamlit
st.dataframe(df_melted)

st.write("The data is rather difficult to work with in this state as it is all in one table.")
st.write("The 'Value of Issues by Seller column includes multiple variables: decade and seller. \
         We will need to separate these variables and create new tables for each seller")
st.divider()
#_________________________________________________________________
#----Creating new tables and separating the variables----

# Create new columns for the decade and seller. Lines 23 and 24 were generated from ChatGPT 
df_melted["Decade"] = df_melted["Value of Issues by Seller"].str.extract(r'(\d{2}s)')
df_melted["Seller"] = df_melted["Value of Issues by Seller"].str.extract(r'_(\w+)$')

# Reorder columns and delete the 'Value of Issues by Seller' column
df_melted = df_melted[["Member", "Seller", "Decade", "Value"]]

# Create a new table for each seller
df_heritage = df_melted[df_melted["Seller"] == "heritage"]
df_ebay = df_melted[df_melted["Seller"] == "ebay"]
df_wiz = df_melted[df_melted["Seller"] == "wiz"]
df_oStreet = df_melted[df_melted["Seller"] == "oStreet"]

# Delete empty rows from each table
df_heritage = df_heritage.dropna()
df_ebay = df_ebay.dropna()
df_wiz = df_wiz.dropna()
df_oStreet = df_oStreet.dropna()

#_________________________________________________________________
# ----Heritage Seller data and visualizations----

# Set header for Heritage seller section in Streamlit
st.subheader("Values from Heritage Seller by Decade")

# Introduce the cleaned up table
st.write("The following table as split up the seller and decade variables into their own columns")
st.write("Missing data has also been removed.")

# Display the table in Streamlit
st.dataframe(df_heritage)

# Introduce the data visualization
st.divider()
st.write("Now we can visualize the data clearly. To do this we will be using bar plots and scatter plots")

# Create a bar plot of the Heritage seller data
fig, ax = plt.subplots()
sns.barplot(x="Decade", y="Value", data = df_heritage)

# Label the visualization: title and axis labels
ax.set_title("Average Value by Decade - Heritage Seller")
ax.set_xlabel("Decade")
ax.set_ylabel("Value")

# Display the bar plot in Streamlit
st.pyplot(fig)

# Create a scatter plot of the Heritage seller data
fig, ax = plt.subplots()
sns.scatterplot(x="Decade", y="Value", data = df_heritage)

# Label the visualization: title and axis labels
ax.set_title("Individual Values by Decade - Heritage Seller")
ax.set_xlabel("Decade")
ax.set_ylabel("Value")

# Display the scatter plot in Streamlit
st.pyplot(fig)

#_________________________________________________________________

# Set up the remaining three datasets and their visualizations
st.divider()
st.write("The data will be presented in the same way for the other three sellers. Please see below.")
st.divider()

#_________________________________________________________________
# ----eBay Seller data and visualizations----

# Set header for eBay seller section in Streamlit
st.subheader("Values from eBay Seller by Decade")

# Display the table in Streamlit
st.dataframe(df_ebay)

# Create a bar plot of the eBay seller data
fig, ax = plt.subplots()
sns.barplot(x="Decade", y="Value", data = df_ebay)

# Label the visualization: title and axis labels
ax.set_title("Average Value by Decade - eBay Seller")
ax.set_xlabel("Decade")
ax.set_ylabel("Value")

# Display the bar plot in Streamlit
st.pyplot(fig)

# Create a scatter plot of the eBay seller data
fig, ax = plt.subplots()
sns.scatterplot(x="Decade", y="Value", data = df_ebay)

# Label the visualization: title and axis labels
ax.set_title("Individual Values by Decade - eBay Seller")
ax.set_xlabel("Decade")
ax.set_ylabel("Value")

# Display the scatter plot in Streamlit
st.pyplot(fig)

#_________________________________________________________________
# ----Wiz Seller data and visualizations----
st.divider()
# Set header for Wiz seller section in Streamlit
st.subheader("Values from Wiz Seller by Decade")

# Display the table in Streamlit
st.dataframe(df_wiz)

# Create a bar plot of the Wiz seller data
fig, ax = plt.subplots()
sns.barplot(x="Decade", y="Value", data = df_wiz)

# Label the visualization: title and axis labels
ax.set_title("Average Value by Decade - Wiz Seller")
ax.set_xlabel("Decade")
ax.set_ylabel("Value")

# Display the bar plot in Streamlit
st.pyplot(fig)

# Create a scatter plot of the Wiz seller data
fig, ax = plt.subplots()
sns.scatterplot(x="Decade", y="Value", data = df_wiz)

# Label the visualization: title and axis labels
ax.set_title("Individual Values by Decade - Wiz Seller")
ax.set_xlabel("Decade")
ax.set_ylabel("Value")

# Display the scatter plot in Streamlit
st.pyplot(fig)

#_________________________________________________________________
# ----oStreet Seller data and visualizations----
st.divider()
# Set header for oStreet seller section in Streamlit
st.subheader("Values from oStreet Seller by Decade")

# Display the table in Streamlit
st.dataframe(df_oStreet)

# Create a bar plot of the oStreet seller data
fig, ax = plt.subplots()
sns.barplot(x="Decade", y="Value", data = df_oStreet)

# Label the visualization: title and axis labels
ax.set_title("Average Value by Decade - oStreet Seller")
ax.set_xlabel("Decade")
ax.set_ylabel("Value")

# Display the bar plot in Streamlit
st.pyplot(fig)

# Create a scatter plot of the oStreet seller data
fig, ax = plt.subplots()
sns.scatterplot(x="Decade", y="Value", data = df_oStreet)

# Label the visualization: title and axis labels
ax.set_title("Individual Values by Decade - oStreet Seller")
ax.set_xlabel("Decade")
ax.set_ylabel("Value")

# Display the scatter plot in Streamlit
st.pyplot(fig)