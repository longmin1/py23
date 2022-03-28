import re

# pattern=r"hogwarts"
# prog=re.compile(pattern)

# 匹配以hog开头的字符串
import time

pattern=r"hog\w+"

s='Hogwarts school,i love hogwarts'
result=re.findall(pattern,s,re.I)
print(result)

s1='today i am in hogwarts xx hogwarts  hogwarts'
result1=re.findall(pattern,s1,re.I)
print(result1)


