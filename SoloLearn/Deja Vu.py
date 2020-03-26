import re,math
def regForm(searchKey):
	return re.compile('('+searchKey+'){2,}')
str=input().strip()
# str=' This ispstpst'.strip()
ans=''
isFound=False
while True:
    for w in str:
        st=''
        pos=str.find(w)
        reg=regForm(w)
        m1=reg.search(str)
        if m1:
            ans=m1.group()
            isFound=True
            break
        else:
            if w == str[len(str)-1]:
                isFound =True
            else:
                if len(st) < len(str):
                    for c in range(pos,len(str)):
                        st += str[c]
                        reg=regForm(st)
                        m2=reg.search(str)
                        if m2:
                            ans=m2.group()
                            isFound=True
                            break
    if isFound or len(ans)>0:
        break
if len(ans)>0:
    print('Deja Vu')
else:
    print('Unique')