# README

## Overview

This project is designed to scrape current affairs quiz questions and answers from the GKToday website, extract relevant information, and save it to markdown files. The information is saved in date-specific markdown files, and the file creation dates are adjusted to reflect the actual dates of the articles.

## Requirements

- Python 3.x
- Required libraries: `requests`, `beautifulsoup4`, `pywin32`

## Setup

1. **Clone the repository** or download the script.
2. **Install the required libraries** using pip:
   ```bash
   pip install requests beautifulsoup4 pypiwin32
   ```

3. **Set the base directory** where the markdown files will be saved:
   ```python
   base_dir = "C:\\Users\\..."
   ```
   Remember to use '\\\\' instead of the windows default '\\'

## Usage

1. **URL Setup**:
   Change the URL variable to the target webpage containing the <article> tags you wish to scrape:
   ```python
   url = "https://www.gktoday.in/gk-current-affairs-quiz-questions-answers/"
   ```

2. **Run the Script**:
   Execute the script:
   ```bash
   python script_name.py
   ```
   The script will parse the articles from the given URL, extract the titles, dates, and notes, and save them in date-specific markdown files.

## Functions

### parse_articles_from_url(url, file_name)

- **Parameters**:
  - `url` (str): The URL containing the <article> tags.
  - `file_name` (str): The name of the file to which the information will be appended (not currently used in the script).

- **Description**:
  This function sends a GET request to the provided URL, parses the HTML content, finds all <article> tags, and iterates through the links within these tags. For each link, it calls the `parse_page` function to extract and save the content.

### parse_page(url, base_dir, processed_urls, creation_time)

- **Parameters**:
  - `url` (str): The URL of the page to parse.
  - `base_dir` (str): The base directory where the markdown files will be saved.
  - `processed_urls` (set): A set of URLs that have already been processed to avoid duplication.
  - `creation_time` (datetime): The timestamp to set as the creation time for the markdown files.

- **Description**:
  This function sends a GET request to the provided URL, parses the HTML content, extracts the title, date, and notes, and saves this information in a markdown file named after the date. The file creation time is set to reflect the actual date of the article.

## Notes

- The script sets the creation time of the markdown files to reflect the actual date of the articles. This functionality uses the `pywin32` library, which works on Windows OS.
- Ensure the `base_dir` exists before running the script, or the script will fail when trying to write the files.

## Example

Here's an example of how to use the script:

1. Set the `url` to the target webpage:
   ```python
   url = "https://www.gktoday.in/gk-current-affairs-quiz-questions-answers/"
   ```

2. Set the `base_dir` to your desired directory:
   ```python
   base_dir = "C:\\Users\\..."
   ```
   Remember to use '\\\\' instead of the windows default '\\'

3. Run the script to fetch and save the current affairs data.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

If you encounter any issues or have questions, feel free to open an issue or contact the project maintainer.
