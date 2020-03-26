import math
import re
reg0=re.compile(r'[0-9.]+')
reg=re.compile(r'(\d)+.?(\d){3}')
num_str=input('so: ').strip()
m=reg0.match(num_str)
if m:
    number=float(m.group())
    square=reg.match(str(number**2)).group()
    root=reg.match(str(math.sqrt(number))).group()
    print(square)
    print(root)
else:
    print('Invalid Number')