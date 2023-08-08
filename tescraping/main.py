from bs4 import BeautifulSoup
import requests

url = 'https://www.youtube.com'
res = requests.get(url).text
soup = BeautifulSoup(res,'lxml')

print(type(soup))