import openpyxl

#open the xl file(Workbook)
wb=openpyxl.open("/Users/vishnu/Downloads/Python-Selenium/Book1.xlsx")
print(type(wb))
sh=wb['Sheet1'] #goto sheet1
v=sh.cell(1,1).value  #get the value present in row-1 col-1
print(v)    #print it
wb.close()  #close

