import re
reg=re.compile(r'(\d){5}')
code=input('Code:').strip()
m=reg.match(code)
if m:
    ans='true'
else:
    ans='false'
print(ans)