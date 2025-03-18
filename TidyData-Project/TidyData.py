import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#_________________________________________________________________
# Import the Mutant Moneyball dataset
df = pd.read_csv("mutant_moneyball.csv")

# Melt the dataframe
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

#_________________________________________________________________

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

# Display the table in Streamlit
st.dataframe(df_heritage)

# Create a histogram of the data
st.subheader("Heritage")
fig, ax = plt.subplots()
sns.histplot(df_heritage, kde = True)

# Label the visualization: title and axis labels
ax.set_title("Total Value by Decade - Heritage Seller")
ax.set_xlabel("Decade")
ax.set_ylabel("Total Value")
st.pyplot(fig)

#_________________________________________________________________

# Create the plot
fig, ax = plt.subplots()
sns.barplot(x="Decade", y="Value", data=df_heritage)

# Add titles and labels
ax.set_title("Total Value by Decade - Heritage Seller")
ax.set_xlabel("Decade")
ax.set_ylabel("Total Value")

# Display the plot in Streamlit
st.pyplot(fig)

fig, ax = plt.subplots()
sns.scatterplot(x="Decade", y="Value", data = df_heritage)
st.pyplot(fig)





st.dataframe(df_ebay)
st.dataframe(df_wiz)
st.dataframe(df_oStreet)