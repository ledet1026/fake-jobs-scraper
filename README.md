# fake-jobs-scraper
A Python web scraping project that extracts job postings and contact emails from a sample job board. Demonstrates modular scraping, data parsing, email extraction, and structured data storage using Python, BeautifulSoup, and pandas.

The scraper:
- Extracts job **title, company, location, and application link**
- Searches for **emails** present on the page using regex
- Stores structured data using **pandas DataFrame**
- Demonstrates modular coding with **functions** for fetching and parsing pages

Important: This scraper is designed for educational purposes only and targets a practice site.  Do not scrape websites without proper authorization.

---
## Features
- Fetch HTML content from the target website
- Parse job postings using BeautifulSoup
- Extract key details: job title, company, location, apply links
- Search for emails on the page using regular expressions
- Convert extracted data into a structured DataFrame
- Ready to extend: CSV export, keyword filtering, or multi-page scraping

---

## Requirements
- Python 3.x
- Libraries:
    -requests
    -beautifusoup4
    -pandas
    -re(built-in)
    -time(built-in)

Install libraries using pip:

```bash
pip install requests beautifulsoup4 pandas

How to run code


main.py



