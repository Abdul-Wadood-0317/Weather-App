# This program uses BeautifulSoup to scrape Urdu text from a news article.

from bs4 import BeautifulSoup
import requests

# Define the URL of the news article
url = "https://www.bolnews.com/urdu/"

# Send a GET request to the URL and store the response
response = requests.get(url)
print(response)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all paragraphs containing Urdu text
    paragraphs = soup.find_all("p", lang="ur")

    # Extract the text from each paragraph and store it in a list
    urdu_text = []
    for paragraph in paragraphs:
        urdu_text.append(paragraph.text)
    
    # Print the extracted Urdu text
    print("\n".join(urdu_text))
else:
    print(f"Error: Could not access the URL. Status code: {response.status_code}")
#code is my life now,i have 