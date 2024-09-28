import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

# Function to scrape the website using Selenium
# It launches a Chrome browser instance, loads the webpage, and returns the HTML content
def scrape_website(website):
    # Inform the user that the Chrome browser is being launched
    print("Launching chrome browser.....")

    # Path to the Chrome WebDriver executable (chromedriver.exe)
    chrome_driver_path = "chromedriver.exe"

    # Set options for the Chrome WebDriver
    options = webdriver.ChromeOptions()

    # Initialize the Chrome WebDriver with the provided service and options
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        # Navigate to the specified website
        driver.get(website)
        print("Page loaded......")

        # Get the HTML content of the webpage
        html = driver.page_source

        # Pause for 20 seconds to allow dynamic content to load (if applicable)
        time.sleep(20)

        # Return the HTML content of the page
        return html

    # Ensure the browser is properly closed after scraping is done
    finally:
        driver.quit()

# Function to extract the body content from the HTML page using BeautifulSoup
def extract_body_content(html_content):
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract the <body> tag and its content
    body_content = soup.body

    # If body content exists, return it as a string; otherwise, return an empty string
    if body_content:
        return str(body_content)
    return ""

# Function to clean the body content by removing script and style elements
def clean_body_content(body_content):
    # Parse the body content with BeautifulSoup
    soup = BeautifulSoup(body_content, "html.parser")

    # Remove all <script> and <style> tags from the body content
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get the text content of the body, separating lines with newline characters
    cleaned_content = soup.get_text(separator="\n")

    # Clean up the text by stripping excess whitespace from each line and removing empty lines
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    # Return the cleaned text content
    return cleaned_content

# Function to split the DOM content into chunks of a maximum specified length (default is 6000 characters)
def split_dom_content(dom_content, max_length=6000):
    # Use list comprehension to divide the DOM content into smaller chunks
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]
