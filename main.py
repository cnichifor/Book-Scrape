import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")