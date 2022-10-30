from bs4 import BeautifulSoup
import requests

data = requests.get('https://www.goldtraders.or.th/')
print(data)