import re
reg=re.compile(r'HB*P')
letters=input('String: ').strip().upper()
blocks_num=reg.search(letters)
if blocks_num:
    print(len(blocks_num.group(0))-2) # do not count H and P
else:
    print(0)