try:
    s=['a','c']
    n=[0,2]
    s[1:1]='b'
    n[1:1]=1
except :
    pass
else:
    print(s[1],n[1])