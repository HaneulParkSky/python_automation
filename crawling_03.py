
# https://class101.net/classes/5e6c5ef82c45b20dc455e7b6/contents/5e8ff5d114aa3d6d0f5c0782
# 템플릿 1 : 크롤링(타이틀)

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

print(crawling_template('https://davelee-fun.github.io/blog/crawl_test_css', 'li.course.paid'))



# CSS Selector 선택 : 하위 태그 선택
# 띄어쓸 때는 상위 태그 안에 해당 태그가 있기만 하면 선택 가능
    # items = soup.select('ul a')
# ">"는 상위 태그 바로 아래 해당 태그가 있어야 함
    # items = soup.select('ul > li')
