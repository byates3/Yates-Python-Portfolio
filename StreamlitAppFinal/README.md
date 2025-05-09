**Skyrim Book Identification and Named Entity Recognition App for Streamlit**

**Project Overview**
---

This is an interactive app for Streamlit that enables users to explore the 536 books of The Elder Scrolls V: Skyrim using filter optinos and Named Entity Recognition (NER). Users may filter via author and via whether a book grants a skill boost or not. The app provides a short description of the selected book. NER allows the user to determine the contents of the book. The amount of books in this game is daunting, and this app aims to make the process of navigating these books much simpler. Whether users want to determine which books provide skill boosts or simply find an interesting read to expand their lore knowledge, this app is here to help! No coding experience is necessary to understand this project; simply navigate to the Streamlit Cloud link in the instructions section to explore the app!

-------------------------------------------------------------------------

**Instructions**
---

Deployed app on Streamlit Cloud:
https://byates3-nerstapp.streamlit.app/

Running the app locally:

    Download the entire StreamlitAppFinal folder including: SkyrimApp.py, README.md, book.jpg, skyrim_books.csv, skyrim_logo.jpg, and requirements.txt

    To install spaCy locally:

    !pip install spacy
    !python -m spacy download en_core_web_sm

    Ensure that there is only one version of Streamlit being used in the requirements.txt file.

    To launch the app:

    In the terminal: cd StreamlitAppFinal (Depending on where the folder is saved, you may need to cd into other folders before you can cd into StreamlitAppFinal)
    Then in the terminal, use the following command: streamlit run ./SkyrimApp.py

    This will default to opening a new tab in your primary web browser. This tab will load the Streamlit app.

-------------------------------------------------------------------------

**App Features**
---

**Filter**

Users may filter through the 536 books by author and by skill point grants. Most authors only have one or two books, but some wrote entire volumes. This app enables users to find favorite authors, determine book titles for side quests, or quickly level up their character using books.

**Named Entity Recognition**

Once a user selects a book, the app will give a short description of the text and, using spaCy's natural language processing capabilities, recognize any relevant entities. This is especially helpful for gamers to identify characters, factions, or locations within the text.

**Visualization**

Skyrim is a huge game even without the 536 books. It is nearly impossible to explore everything, and this app visualizes the book data to put this into perspective. It also gives users the opportunity to find what they need more efficiently.

-------------------------------------------------------------------------

**References**
---

spaCy overview: https://spacy.io/api
Dataframe source: https://www.kaggle.com/datasets/aadamg/skyrim-books-from-uesp?resource=download

For any issues, please message Beau Yates, byates3 on GitHub.

-------------------------------------------------------------------------