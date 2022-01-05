import re
num="44580917".strip()
reg=re.compile(r"^[189]")
if (len(num)==8 and num.isdigit() and reg.match(num)):
    print("Valid")
else:
    print("Invalid")