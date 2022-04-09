import csv
import pytest
def add(x,y):
    return int(x)+int(y)

def get_csv():
    with open('./data.csv','r',encoding='utf-8')as f:
        csv_date=csv.reader(f)
        # print(csv_date)#<_csv.reader object at 0x00000143DB943B38>
        csv_value=[]
        for i in csv_date:
            csv_value.append(i)
        # print(csv_value)#[['1', '2', '3'], ['4', '5', '9'], ['7', '8', '15']]
    return csv_value

# @pytest.mark.parametrize('x,y,excepted',[[1,1,2],[2,3,5]])
@pytest.mark.parametrize('x,y,excepted',get_csv())
def test_case(x,y,excepted):
    # print(get_csv())
    assert add(x,y)==int(excepted)
