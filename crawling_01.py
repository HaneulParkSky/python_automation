
# 웹페이지 파싱(분석)하기

import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test_css')


# res에 웹페이지 객체가 저장되며, 웹페이지 데이터를 res.content 내부변수에서 불러올 수 있음 
soup = BeautifulSoup(res.content, 'html5lib')

# soup.select() 함수를 사용해서, 해당 데이터를 리스트 형태로 가져옴
# 리스트의 각 아이템을 반복문으로 추출하고, item.get_text()로 실제 데이터를 가져올 수 있음

datas1 = soup.select('li')
for item in datas1:
    print(item.get_text())





