import re
word="45awHal44gb8"
word="12545phatM"
pat1=r"[A-Z]+.*"
pat2=r"[0-9]+.*"
# pat=r"[0-9]+[A-Z]+"print(m.group())
m=re.search(pat1,word)
if m:
    # print(m)
    # print(m.group(0))
    m2=re.search(pat2,word)
    if m2:
        print(m2.group(0))
        print("Match")
    else:
        print("No match")
else:
    print("no Match")