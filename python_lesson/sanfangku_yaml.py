import yaml

python_data={'name': 'junxi', 'age': 18, 'spouse': {'name': 'Rui', 'age': 18}, 'children': [{'name': 'Chen You', 'age': 3}, {'name': 'Ruo Xi', 'age': 2}]}
#写入到my.yaml的文件中
with open('my.yaml','w',encoding='utf-8')as f:
    yaml.dump(python_data,f)

#读取yaml文件
data=yaml.safe_load(open('my.yaml', 'r', encoding='utf-8'))
print(data,type(data))