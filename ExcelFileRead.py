#How to  read excel file using selenium
#code by sunil Savale
#date - 24/09/2021

import xlrd


#create a Variable to open a file
workbook = xlrd.open_workbook("D:\XLRDfile.xls")
sheet = workbook.sheet_by_name("Details")

#Get the total number of row
rowCount = sheet.nrows
columsCount = sheet.ncols
print(rowCount)
print(columsCount)

#get the data from excel sheet using a for loop
for current_row in range(1, rowCount):
    names = sheet.cell_value(current_row, 0)
    surname = sheet.cell_value(current_row, 1)
    location = sheet.cell_value(current_row, 2)

    print(names + " " + surname + " " + location)