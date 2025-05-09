#-------------------------------------
#-------------------------------------
#------- Skyrim Books App ------------
#------- Final Streamlit App ---------
#------- Written by Beau Yates -------
#-------------------------------------
#-------------------------------------


#---------------------------------------------------
# Part 1: Import libraries and initialize Dataframe
#---------------------------------------------------

# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import spacy

# Load spaCy's natural language processing library
nlp = spacy.load("en_core_web_sm")

# Load dataframe
def loadData():
    return pd.read_csv("StreamlitAppFinal/skyrim_books.csv")

# Define dataframe as a varibale 'df'
df = loadData()

# Change all columns to lower case and strip unneeded characters/spaces
df.columns = df.columns.str.strip().str.lower()


#--------------------------------------
# Part 2: Initialize the Streamlit App
#--------------------------------------

# Add Skyrim logo image to top of app page
st.image("skyrim_logo.jpg")

# Create a title and link to original dataframe website
st.title("Skyrim Books Exploration")
st.divider()
st.write("This app uses the Skyrim Books dataset that can be found at the following link: \
         https://www.kaggle.com/datasets/aadamg/skyrim-books-from-uesp?resource=download")
st.divider()

# Introductory paragraph to the topic of Skyrim books. Make the topic clear even for those who have not played the game before
st.write("The Elder Scrolls V: Skyrim is a game that many have experienced and loved since its release in 2011.\
         While most would praise the game primarily for its worldbuilding, cities, or side quests, one under appreciated\
         aspect of the game is its books. There are 337 individual titles in Skyrim, some of which come in volumes, making the total\
         of individual books 536. These books grant skill boosts, expand the lore of the game, present\
         local folk tales, and can even serve as cookbooks.")
st.divider()

# Insert example image of a Skyrim book in game
st.image("book.jpg")
st.divider()

# Introductory paragraph to the goals of the app
st.write("This app aims to make the navigation of Skyrim's books easier than ever. Filter options can be found in the tab on\
         the left of the page. Users will find a short description\
         of their selected book at the bottom of the page. With Named Entitiy Recognition (NER), users may discern\
         whether a book contains relevant information to them. Whether it be finding certain folk heros or even just a sweet roll recipe,\
         let's have some and explore this niche aspect of Skyrim!")

st.divider()


#----------------------------
# Part 3: Data Visualization
#----------------------------

# Title and description for pie chart section
st.subheader("How many books actually grant skills?")
st.write("As you can see in the following pie chart, only about 1/6 of the books in Skyrim actually grant\
         skill points to the player.")

# Create variable 'skill_counts' to determine number of books that grant a skill boost
skill_counts = df["skill"].dropna().value_counts()

# Initialize the pie chart
fig, ax = plt.subplots()
skill_counts.plot(kind="pie")

# Set axis labels
ax.set_xlabel("'0' represents no skills. '1' represents a skill grant.")
ax.set_ylabel("")

# Set title on the pie chart itself
ax.set_title("Number of Books Grant Skill Points")

# Display chart in Streamlit app
st.pyplot(fig)

st.divider()


#------------------------
# Part 4: Filter Options
#------------------------

# Create a side tab for users to determine their filter options
st.sidebar.header("Filter Options")

# Checkbox to filter books that grant skill boost
skill_only = st.sidebar.checkbox("Show only books that raise a skill")

# Dropdown select box for users to select an author
authors = df["author"].dropna().unique()
selected_author = st.sidebar.selectbox("Search by Author", options=["All"] + sorted(authors.tolist()))

# Copy the dataframe into a new filtered variable
filtered_df = df.copy()

# If the user does not select option 'All' in dropdown, filter to just the selected author
if selected_author != "All":
    filtered_df = filtered_df[filtered_df["author"] == selected_author]

# If the user checks the 'Show only books that raise a skill' box, filter as needed
if skill_only:
    # The notna() in the following line was written with assistance from ChatGPT
    filtered_df = filtered_df[filtered_df["skill"].notna() & (filtered_df["skill"] == 1)]


#----------------------------------------
# Part 5: List of filtered Skyrim books
#----------------------------------------

# When the app is launched, this list dafaults to displaying all the books in the game

# Title and description for list section
st.subheader("Filtered Book List")
st.write("Below are all selected books. To modify your selection, use the 'Filter Options' tab on\
         the left of the page.")

# Display the filtered list
st.dataframe(filtered_df[["title", "author", "skill"]])

st.divider()


#----------------------------------
# Part 6: Named Entity Recognition
#----------------------------------

# Create title for section
st.subheader("Named Entity Recognition")

# Dropdown for user to select a book from their filtered list
# Note: Many authors only have one or two books, though some can many more
selected_book = st.selectbox("Select a Book for NER", filtered_df["title"].unique())

# The following line was written with assistance from ChatGPT
book_text = filtered_df[filtered_df["title"] == selected_book]["description"].values[0]

# Write out the full book description as provided by the dataframe 'description' column
st.text_area("Book Description", book_text)

# When a user presses the 'Run NER' button, display all recognized entities
if st.button("Run NER"):
    doc = nlp(book_text)
    ents = [(ent.text, ent.label_) for ent in doc.ents]
    st.write(f"Entities found: {len(ents)}")
    # The following 2 lines were generated by ChatGPT
    for ent, label in ents:
        st.markdown(f"- **{ent}** ({label})")