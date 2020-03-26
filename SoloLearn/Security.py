import re
reg=re.compile(r'T(X)*\$|\$(X)*T')
str=input('Money Flow: ').strip()
str=str.upper()
if len(str) >0 :
    m=reg.search(str)
    if m:
        isSafe=False
    else:
        isSafe=True
    print('quiet' if isSafe else 'ALARM')