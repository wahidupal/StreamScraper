import streamlit as st
from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content,                
)
from parse import parse_with_ollama

# Set the title of the Streamlit app
st.title("AI Web Scraper")

# Create an input box for the user to enter a website URL
url = st.text_input("Enter a Website URL: ")

# When the user presses the 'Scrape Site' button, the following code is executed
if st.button("Scrape Site"):
    # Inform the user that the website scraping is in progress
    st.write("Scraping the website")

    # Call the 'scrape_website' function to fetch the HTML content of the website entered by the user
    result = scrape_website(url)

    # Extract only the body content from the full HTML using 'extract_body_content'
    body_content = extract_body_content(result)

    # Clean the extracted body content using 'clean_body_content'
    cleaned_content = clean_body_content(body_content)

    # Store the cleaned DOM content in the session state so that it's accessible later
    st.session_state.dom_content = cleaned_content

    # Provide an expandable section to view the cleaned DOM content
    with st.expander("View DOM Content"):
        # Display the cleaned DOM content in a text area (scrollable)
        st.text_area("DOM Content", cleaned_content, height=300)

# If there's DOM content already stored in session state, show options for parsing
if "dom_content" in st.session_state:
    # Provide a text area where the user can describe what content they want to parse
    parse_description = st.text_area("Describe what you want to parse?")

    # When the 'Parse Content' button is pressed, execute the following block
    if st.button("Parse Content"):
        # Check if the user has provided a description for parsing
        if parse_description:
            # Inform the user that parsing is in progress
            st.write("Parsing the content")

            # Split the cleaned DOM content into chunks to make it easier to process
            dom_chunks = split_dom_content(st.session_state.dom_content)

            # Parse the DOM content based on the user's input description using 'parse_with_ollama'
            result = parse_with_ollama(dom_chunks, parse_description)

            # Display the result of the parsing operation
            st.write(result)
