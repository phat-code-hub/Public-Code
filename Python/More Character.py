import re
pw=input()
reg1=re.compile(r"[A-Z]*")
reg2=re.compile(r"\d*")
regs=[reg1,reg2]
ls=[]
for reg in regs:
    m=reg.findall(pw)
    if m:
        zero=[s!='' for s in m]
        ls.append(any(zero))
print("Password created" if all(ls) else "Wrong format")