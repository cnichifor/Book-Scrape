# BookScrape

A simple Python script that scrapes book titles from [Books to Scrape](https://books.toscrape.com/) using `requests` and `BeautifulSoup`.

---

## Project Overview

`bookscrape.py` retrieves the homepage of the Books to Scrape demo site, parses its HTML to locate book entries, and prints the title of each book to the console.

---

## File Structure

```
├── bookscrape.py    # Main scraping script
└── requirements.txt # List of Python dependencies (optional)
```

---

## Prerequisites

* **Python 3.7+**
* **pip** for installing dependencies

---

## Installation

1. **Clone or download** the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **(Optional) Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

> **requirements.txt** should contain:
>
> ```text
> requests
> beautifulsoup4
> ```

---

## Usage

Run the script directly with Python:

```bash
python bookscrape.py
```

It will output a list of book titles, for example:

```
A Light in the Attic
Tipping the Velvet
Soumission
... (and so on)
```

---

## How It Works

1. **HTTP Request**: Fetches the page content of `https://books.toscrape.com/` using `requests.get`.
2. **HTML Parsing**: Uses `BeautifulSoup` to parse the response and find the main `<section>` containing product cards.
3. **Data Extraction**: Locates all `<article class="product_pod">` elements, extracts the `title` attribute from the `<a>` tag within each `<h3>`, and collects it in a list.
4. **Output**: Prints each title on its own line.

---

## Potential Improvements

* **Pagination**: Iterate through all pages to scrape every book rather than just the first page.
* **Error Handling**: Check status codes and catch network or parsing exceptions.
* **CLI Arguments**: Allow the user to specify a URL or output file via command-line flags (e.g., `--url`, `--output`).
* **Data Storage**: Save the results to CSV or JSON instead of printing to stdout.
* **Rate Limiting**: Add delays between requests to respect server load.

---

## License

This script is provided under the MIT License. Feel free to use and adapt it for your own scraping projects.
