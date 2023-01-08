import urllib.request as fetch
from bs4 import BeautifulSoup

url = input('Enter Url: ')
html = fetch.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags
elements = soup.find_all('span')

total: int = 0
count: int = 0

for element in elements:
    element_number = int(element.contents[0])
    total += element_number
    count += 1

print(total, count)
