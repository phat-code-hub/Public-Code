import re
reg=re.compile(r'.\s.')
# words=input('Nhap: ').strip
words='This string gets stucks'
m=reg.findall(words)
if m:
    ans= all([x[0]== x[-1] for x in m])
    print('true' if ans else 'false')
else:
    print('Nothing')