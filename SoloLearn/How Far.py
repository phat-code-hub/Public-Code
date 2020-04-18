import re
reg=re.compile(r'H{1}B*P{1}|P{1}B*H{1}')
letters=input('String: ').strip().upper()
blocks_num=reg.search(letters)
if blocks_num:
    print(len(blocks_num.group(0))-2) # do not count H and P
else:
    print(0)