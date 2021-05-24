
# 템플릿
# 엑셀 파일 읽어서 리스트 변수로 가져오기

import openpyxl

def read_excel_template(filename, sheetname):
    excel_file = openpyxl.load_workbook(filename)

    if sheetname == '':         # sheet 이름이 없다면, 
        excel_sheet = excel_file.active   # 디폴트로 가져올 수 있는 sheet가 선택됨
    else:
        excel_sheet = excel_file[sheetname]

    return_data = list()
    for item in excel_sheet.rows:
        datas1 = list()
        for item2 in item:
            datas1.append(item2.value)
        return_data.append(datas1)

    excel_file.close()
    return return_data

datas1 = read_excel_template('shop_in_seoul.xlsx','fastfood')
