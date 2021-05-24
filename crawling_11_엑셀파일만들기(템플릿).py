

# 템플릿 : 리스트 변수 데이터를 엑셀 파일로 만들기

import openpyxl

def write_excel_template(filename, sheetname, listdata):
    excel_file = openpyxl.Workbook()
    excel_sheet = excel_file.active

    if sheetname != '':
        excel_file.title = sheetname

    for item in listdata:
        excel_sheet.append(item)
    excel_file.save(filename)
    excel_file.close()
    

datas1 = read_excel_template('shop_in_seoul.xlsx','')

write_excel_template('testexcel.xlsx','리포트',datas1)
