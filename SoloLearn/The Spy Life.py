import re
reg=re.compile(r'[a-zA-Z ]')
str=input('Nhap Chuoi ').strip()
str=str[::-1]
words=reg.findall(str)
wh=''.join(words)

print(wh)