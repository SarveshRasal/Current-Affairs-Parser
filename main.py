import requests
import os
from bs4 import BeautifulSoup
import pywintypes
import win32file
import win32con
from datetime import datetime, timedelta

# Function to parse a webpage given its URL and append the title and URL to a file
def parse_page(url, base_dir, processed_urls, creation_time):
    if url in processed_urls:
        print("URL already processed:", url)
        return

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the title of the webpage
        title = soup.title.text

        # Extract date
        date = soup.find(class_='meta_date').text.strip()
        print(date)

        # Extract all the notes within it
        notes = soup.find_all(class_='answer_hint')
        hints = []

        for note in notes:
            list_br = note.find_all('br')
            for item in list_br:
                hint = item.next_sibling.strip()
                hints.append(hint)

        # Write hints to a file named after the date
        with open(f"{base_dir + date}.md", 'a', encoding='utf-8') as f:
            f.write("### Current Affairs\n")
            f.write(f"URL: {url}\n\n")
            for hint in hints:
                f.write(hint + '\n\n')
            f.write('\n')

        fh = win32file.CreateFile(
            f"{base_dir + date}.md",
            win32con.GENERIC_WRITE,
            0,
            None,
            win32con.OPEN_EXISTING,
            win32con.FILE_ATTRIBUTE_NORMAL,
            None
        )

        win32file.SetFileTime(fh, creation_time, None, None)
        print(creation_time)

    else:
        print("Failed to fetch the webpage:", url)


# Function to visit and parse all links within <article> tags from a given URL
def parse_articles_from_url(url, file_name):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all <article> tags
        article_tags = soup.find_all('article')

        # Initialize a set to store processed URLs
        processed_urls = set()

        # Extract datetime to set pseudo-functional date_created metadata of files
        creation_time = datetime.now()
        print(creation_time)

        for article_tag in article_tags:
            # Find all <a> tags within the current <article> tag
            link_tags = article_tag.find_all('a')

            for link_tag in link_tags:
                # Get the URL from the href attribute of the <a> tag
                article_url = link_tag.get('href')

                # Subtract a day for next file
                creation_time -= timedelta(days=1)

                # Parse the webpage using the parse_page function
                parse_page(article_url, base_dir, processed_urls, creation_time)

    else:
        print("Failed to fetch the webpage:", url)


# Sample URL containing <article> tags
url = "https://www.gktoday.in/gk-current-affairs-quiz-questions-answers/"
# File name to which the information will be appended
file_name = "parsed_data.txt"
# Base directory where date-wise hint files will be stored
base_dir = "C:\\Users\\justa\\Documents\\My Redemption Arc\\Everyday Things\\"
# Call the parse_articles_from_url function with the URL and file name
parse_articles_from_url(url, file_name)
