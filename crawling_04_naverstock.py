
import requests
from bs4 import BeautifulSoup


def crawling_template(url, css_selector):
    return_data = list()
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html5lib')
    datas1 = soup.select(css_selector)
    for item in datas1:
        return_data.append(item.get_text())
    return return_data

print(crawling_template('https://finance.naver.com/sise', '#popularItemList > li > a'))

