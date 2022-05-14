#openpyxl  的使用
import openpyxl

#获取工作簿
book_excel=openpyxl.load_workbook('python_data.xlsx')

#获取工作表
sheet=book_excel.active

#获取单元格数据的值
a_1=sheet['A1'].value
# print(a_1)#1

c_3=sheet.cell(column=3,row=3).value
# print(c_3)#a

#获取多个单元格的值

cells=sheet['A1':'D5']#--->返回的是一个元组，所以没有value属性，不过可以循环遍历
# print(cells,type(cells))
#((<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>, <Cell 'Sheet1'.D1>),
# (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>, <Cell 'Sheet1'.D2>),
# (<Cell 'Sheet1'.A3>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.C3>, <Cell 'Sheet1'.D3>),
# (<Cell 'Sheet1'.A4>, <Cell 'Sheet1'.B4>, <Cell 'Sheet1'.C4>, <Cell 'Sheet1'.D4>),
# (<Cell 'Sheet1'.A5>, <Cell 'Sheet1'.B5>, <Cell 'Sheet1'.C5>, <Cell 'Sheet1'.D5>)) <class 'tuple'>
