import requests
import json
from bs4 import BeautifulSoup

page = requests.get("https://quotes.toscrape.com/")

soup = BeautifulSoup(page.content, "html.parser")

# Use a single selector to target both quote text and author within the same element
quote_and_author_elements = soup.select(".quote .text")

# Open the JSON file for writing
with open("quotes.json", "w", encoding="utf-8") as json_file:
    for element in quote_and_author_elements:
        # Extract the quote text and author from the element
        quote_text = element.get_text(strip=True)
        author_text = element.find_next("small", class_="author").get_text(strip=True)

        # Create a dictionary for the current quote and write it to the JSON file
        quote_data = {"quote": quote_text, "author": author_text}
        json.dump(quote_data, json_file, ensure_ascii=False, indent=4)
        json_file.write("\n")  # Add a newline between quotes

print("Quotes have been saved to 'quotes.json'")
