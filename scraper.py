import requests
from bs4 import BeautifulSoup, NavigableString, Tag

baseURL = 'https://www.sports-reference.com/cbb/players/carsen-edwards-1.html'

page = requests.get(baseURL)
soup = BeautifulSoup(page.text, 'html.parser')
print(soup)