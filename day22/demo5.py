import openpyxl


wb=openpyxl.open("/Users/vishnu/Downloads/Python-Selenium/Book1.xlsx")
sh=wb['Sheet2']
sh.cell(1,1).value='Bhanu'
wb.save("/Users/vishnu/Downloads/Python-Selenium/Book2.xlsx")#save as
wb.close()