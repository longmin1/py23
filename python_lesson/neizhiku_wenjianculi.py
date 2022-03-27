# f=open('data.txt','r',encoding='utf-8')
# print(f.read())
# f.close()

with open('data.txt','r',encoding='utf-8')as f:
    print(f.read())
    f.seek(0)

    print(f.readline())
    f.seek(0)

    print(f.readlines())
f.close()