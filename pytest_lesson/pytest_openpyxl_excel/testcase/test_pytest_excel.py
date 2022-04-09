#这里实现通过读取excel里的数据，传到下面函数中进行运行
import os

import openpyxl

from pytest_lesson.pytest_openpyxl_excel.func.operation import my_add
import pytest

def test_get_excel():
    """
    读取excel表的值
    :return: 返回这种格式的数据[[1,2,3],[1,5,6]]
    """
    book_excel=openpyxl.load_workbook('../data/add_data.xlsx')
    sheet=book_excel.active
    cells=sheet["A1":"C3"]
    # print(cells)
    list_value=[]
    for cell in cells:
        value_1=[]
        for i in cell:
            # print(i.value)
            value_1.append(i.value)
        list_value.append(value_1)
    return list_value
    # print(list_value)#[[1, 2, 3], [1, 5, 6], [1, 8, 9]]

# @pytest.mark.parametrize('x,y,expected',[[1,2,3],[1,5,6]])
@pytest.mark.parametrize('x,y,expected',test_get_excel())
def test_pytest_excel(x,y,expected):
    assert my_add(x,y)==expected
