**Named Entity Recognition App for Streamlit**

**Project Overview**
---

This is an interactive app for Streamlit that enables users to explore Named Entity Recognition. Users can easily input custom entity patterns and labels, explore the text with full highlights of all entities and their corresponding labels. No coding experience is necessary to understand this project; simply navigate to the Streamlit Cloud link in the instructions section to explore the app!

-------------------------------------------------------------------------

**Instructions**
---

Deployed app on Streamlit Cloud:
https://byates3-nerstapp.streamlit.app/

Running the app locally:

    Download the entire NERStreamlitApp folder including: NERStreamlitApp.py, README.md, and requirements.txt

    To install spaCy locally:

    !pip install spacy
    !python -m spacy download en_core_web_sm

    Ensure that there is only one version of Streamlit being used in the requirements.txt file.

    To launch the app:

    In the terminal: cd NERStreamlitApp (Depending on where the folder is saved, you may need to cd into other folders before you can cd into NERStreamlitApp)
    Then in the terminal, use the following command: streamlit run ./NERStreamlitApp.py

    This will default to opening a new tab in your primary web browser. This tab will load the Streamlit app.

-------------------------------------------------------------------------

**App Features**
---

**Input or Upload Text:**
    - Users are able to either manually input text or upload a .txt file for processing. 

**Add Custom Labels and Patterns:**
    - Users will be able to create as many custom patterns and labels as needed. For example, if a text calls for ficticious characters such as Gandalf, users can add a custom pattern "Gandalf" with the custom label "Wizard". 

**Processed Text**
    - Using spaCy's EntityRuler, all entities will be recognized and labeled according to the spaCy library and to the custom user inputted patterns and labels.
    - Users can view the full hightlighted text with labels in the "Processed Text" section or they can view just the recognized entities and corresponding labels in the "Detected Entities and Labels" section.

-------------------------------------------------------------------------

**References**
---

spaCy overview: https://spacy.io/api

spaCy EntityRuler overview: https://spacy.io/api/entityruler

For any issues, please message Beau Yates, byates3 on GitHub.

-------------------------------------------------------------------------