import re
st='This is 2017'
reg=re.compile(r'[\d]+')
m=reg.match(st)
if m :
    print(m.groups())