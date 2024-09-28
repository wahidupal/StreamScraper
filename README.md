# StreamScraper
## Project Overview

This project implements a dynamic web scraping and parsing tool using **Streamlit** for the frontend, **Selenium** and **BeautifulSoup** for web scraping, and **LangChain-Ollama** for content parsing and information extraction. The app allows users to input a website URL, scrape its content, and extract useful information by providing a parsing description. The tool is powerful, user-friendly, and designed to provide efficient data extraction for various use cases.

### Features

- **Website Scraping**: Utilizes Selenium to scrape the HTML content from any given website.
- **Content Parsing**: Extracts and processes the HTML body content and removes unwanted script and style tags.
- **AI-Powered Parsing**: Uses the Ollama model through LangChain to parse the DOM content according to user-specified descriptions.
- **Interactive Web App**: Built with Streamlit to provide an intuitive and easy-to-use interface.
- **Error Handling**: Ensures that the application remains stable with informative messages for the user.

### User Instructions

To run this app, you need to install the **Ollama AI** on your local machine. Please follow these steps:

1. Go to the official website [here](https://ollama.com/download) and download Ollama.
2. After downloading, follow the installation instructions on the [Ollama GitHub page](https://github.com/ollama/ollama) to install the **llama3.1** model.

**Important Notes:**
- This app includes a 20-second sleep period because you'll need to manually accept cookies when prompted by the website.
- This app will **not work** for websites that require CAPTCHA verification.
