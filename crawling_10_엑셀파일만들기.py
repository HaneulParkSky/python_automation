
# 자동으로 웹사이트 정보를 엑셀 파일로 만들기


# 엑셀 파일 쓰기

import openpyxl

excel_file = openpyxl.Workbook()    #새로운 엑셀파일 생성 함수 -> openpyxl.Workbook()

excel_sheet = excel_file.active
excel_sheet.title = "리포트"   # 디폴트 시트의 이름을 변경함


# 데이터 추가하기

excel_sheet.append(['data1','data2','data3'])

# 엑셀 파일 저장

excel_file.save('testexcel.xlsx') #엑셀파일 저장 save 함수 

# 엑셀 파일 닫기

excel_file.close()






