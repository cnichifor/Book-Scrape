import requests
from bs4 import BeautifulSoup
import time
import csv


site_root = "https://books.toscrape.com"
url = site_root
titles = []

while url:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    cards = soup.find_all("article", class_="product_pod")

    for card in cards:
        header = card.find("h3")
        title = header.find("a")["title"]
        titles.append(title)

    next_a = soup.select_one("li.next > a")
    if next_a:
        href = next_a["href"] 
        url = site_root.rstrip("/") + "/catalogue/" + href.removeprefix("catalogue/")
    else:
        url = None
    print(href)

    
    time.sleep(0.5)

for x in titles:
    print(x, end = "\n")


with open("titles.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title"])         
    for title in titles:
        writer.writerow([title])
print("Saved", len(titles), "titles in titles.csv")