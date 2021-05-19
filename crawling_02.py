
import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css')
soup = BeautifulSoup(res.content, 'html5lib')
datas1 = soup.select('li')
for item in datas1:
    print(item.get_text())

