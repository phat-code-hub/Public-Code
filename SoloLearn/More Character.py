import re
pw=input()
reg1=re.compile(r"[A-Z]*")
reg2=re.compile(r"\d+")
m=reg1.findall(pw)
if m:
    if len(m) >=0:
        zero=list(s!=''  for s in m)
        print(any(zero))
        print("OK")
    else:
        print("NO")
else:
    print("NO FOUND")
