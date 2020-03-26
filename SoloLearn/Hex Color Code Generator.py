import re
reg=re.compile(r'^(\d){,3}$')
red=input('Red :').strip()
green=input('Green: ').strip()
blue=input('Blue: ').strip()
#list up value for validate
checklist=list([red,green,blue])
# check that all values are digits and up to 3 digits
chk=all(reg.match(v)  for v in checklist)
if chk:
    hex_val=[hex(int(v)) for v in checklist]
    #remove hex sign
    RGB=[v[-2:] for v in hex_val]
    hex_Color_Code='#'+''.join(RGB)
    print(hex_Color_Code)
else:
    print('Invalid Color Code')
