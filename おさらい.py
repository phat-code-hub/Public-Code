import re
reg=re.compile(r"#\w+")
text=input().strip()
m=reg.findall(text)
if m:
    for t in m:
        print (t)