
# 웹페이지 주소와 함께 가져오기

import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.drapt.com/e_sale/index.htm?page_name=esale_news&menu_key=34')
soup = BeautifulSoup(res.content, 'html5lib')

datas1 = soup.select('a.c0000000')

for item in datas1:
    print(item.get_text(), 'http://www.drapt.com/e_sale/' + item['href'])

        



