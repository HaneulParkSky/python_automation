
# 업무 자동화를 위한 웹사이트 + 엑셀 파일 만들기


# 1. 웹사이트 정보 추출 자동화 템플릿 선언하기

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


# 2. 엑셀 파일 쓰기 템플릿 선언하기

import openpyxl

def write_excel_template(filename, listdata):
    excel_file = openpyxl.Workbook()
    excel_sheet = excel_file.active

    if sheetname != '':
        excel_sheet.title = sheetname

    for item in listdata:
        excel_sheet.append(item)
    excel_file.save(filename)
    excel_file.close()


# 두가지 기능 한번에 실행하기

datas1 = crawling_template_with_href('http://www.drapt.com/e_sale/index.htm?page_name=esale_news&menu_key=34','a.c0000000','http://www.drapt.com/e_sale/')
write_excel_template('testexcel2.xlsx',datas1)

