import requests
from bs4 import BeautifulSoup

url = "https://app.datacamp.com/learn/courses"

r = requests.get(url)

# print(r.text)

soup = BeautifulSoup(r.text, 'lxml')

tag =soup.div

print(tag.string)
print(tag.attrs)