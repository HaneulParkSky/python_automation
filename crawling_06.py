
# 템플릿 2 : crawling_template_with_href, 크롤링 (타이틀, 웹주소)
# 상세주소 앞에 붙을 주소는 필요 없다면, ''으로 빈 데이터를 호출 하면 됨 

import requests
from bs4 import BeautifulSoup

def crawling_template_with_href(url, css_selector, pre_url):
    return_data = list()
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html5lib')
    datas1 = soup.select(css_selector)
    for item in datas1:
        return_data.append([item.get_text(), pre_url + item['href']])
    return return_data

datas1 = crawling_template_with_href('http://www.drapt.com/e_sale/index.htm?page_name=esale_news&menu_key=34','a.c0000000','http://www.drapt.com/e_sale/')
print(datas1[0],[1])
