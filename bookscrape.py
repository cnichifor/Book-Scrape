import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

section = soup.find("section")
cards = section.find_all("article", class_ = "product_pod")

titles = []
for card in cards:
    header = card.find("h3")
    title = header.find("a")["title"]
    titles.append(title)

for x in titles:
    print(x, end = "\n")