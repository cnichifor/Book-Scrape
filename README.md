# BookScrape

A simple, robust Python scraper that navigates every page of [Books to Scrape](https://books.toscrape.com/), extracts book titles, and writes them to a CSV file.

---

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Script Overview](#script-overview)
6. [Configuration](#configuration)
7. [Project Structure](#project-structure)
8. [Extending & Customizing](#extending--customizing)
9. [Troubleshooting](#troubleshooting)
10. [Contributing](#contributing)
11. [License](#license)

---

## 🚀 Features

* **Automatic Pagination**: Follows the “Next” link on every page until no more remain.
* **Relative URL Resolution**: Builds each next-page URL based on the current page’s folder.
* **CSV Export**: Saves all book titles into `titles.csv` for downstream analysis.
* **Polite Scraping**: Includes a configurable delay between requests to avoid overloading the server.
* **Error Handling**: Uses `raise_for_status()` to abort on HTTP errors.

---

## 🛠️ Prerequisites

* **Python 3.7+**
* [pip](https://pip.pypa.io/en/stable/) package manager

---

## 🧩 Installation

```bash
git clone https://github.com/cnichifor/Book-Scrape.git
cd Book-Scrape
python3 -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
pip install -r requirements.txt
```

> **requirements.txt** should include:
>
> ```
> requests
> beautifulsoup4
> ```

---

## ▶️ Usage

Run the scraper script:

```bash
python bookscrape.py
```

* Prints each title as it’s collected.
* Writes `titles.csv` in the project root when done.

---

## 📝 Script Overview

```python
import requests
from bs4 import BeautifulSoup
import time
import csv

# Configuration
START_URL = "https://books.toscrape.com/"
OUTPUT_CSV = "titles.csv"
DELAY = 1.0
CATALOGUE_ROOT = START_URL.rstrip("/") + "/catalogue/"

# Main
url = START_URL
titles = []
while url:
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # Extract titles
    for card in soup.select("article.product_pod"):
        titles.append(card.select_one("h3 > a")["title"])

    # Find next link
    next_a = soup.select_one("li.next > a")
    if not next_a:
        break
    href = next_a["href"]
    if href.startswith("catalogue/"):
        href = href[len("catalogue/"):]
    # Resolve relative URL
    base_folder = url[:url.rfind("/")+1]
    url = base_folder + href

    time.sleep(DELAY)

# Export to CSV
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title"])
    for title in titles:
        writer.writerow([title])

print(f"Saved {len(titles)} titles to {OUTPUT_CSV}")
```

---

## ⚙️ Configuration

Edit the top of `bookscrape.py`:

```python
START_URL = "https://books.toscrape.com/"
OUTPUT_CSV = "titles.csv"
DELAY = 1.0
```

---

## 📂 Project Structure

```text
Book-Scrape/
├── bookscrape.py      # Main scraper script
├── requirements.txt   # Python dependencies
├── titles.csv         # Output (generated after running)
└── README.md          # This documentation
```

---

## 🔧 Extending & Customizing

* Extract additional fields (price, rating, availability).
* Add JSON or Excel export.
* Implement retry/backoff.
* Add CLI flags with `argparse` or `click`.

---

## 🐞 Troubleshooting

* **404 Errors**: Check URL resolution logic.
* **Missing next link**: Verify `li.next > a` selector.
* **Encoding issues**: Ensure UTF-8 when opening CSV.

---

## 🤝 Contributing

1. Fork it.
2. Create feature branch.
3. Commit changes.
4. Push branch.
5. Open a Pull Request.

---

## 📄 License

MIT © 2025 Cristian Nichifor

> Feel free to fork, adapt, and share!

