import openpyxl

#open the xl file(Workbook)
wb=openpyxl.open("/Users/vishnu/Downloads/Python-Selenium/Book1.xlsx")
v=wb['Sheet1']['A1'].value
print(v)
wb.close()