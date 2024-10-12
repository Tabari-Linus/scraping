from bs4 import BeautifulSoup
import requests

url = "https://app.datacamp.com/learn/courses"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

print(soup.find("div"))