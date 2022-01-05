import re
reg_match= re.compile(r'^(\D)')
reg_number=re.compile(r'\d+')
reg_letter=re.compile(r'\D+|\s*')
words=input('Nhap :').strip()
# words='p3 2h2 at4t·$3k2y'
m=reg_match.match(words)
if m:
    decompressed_text=''
    dGroup=reg_number.findall(words)
    if dGroup:
        digit=[int(n) for n in dGroup if n.isdigit()] 
    lGroup=reg_letter.findall(words)
    if lGroup:
        wGroup=[w for w in lGroup if w!='']
    for i in range(len(digit)):
        decompressed_text += wGroup[i][:-1]+wGroup[i][-1]*digit[i]
    if len(wGroup)>len(digit):
        decompressed_text += wGroup[-1]
    print(decompressed_text)
else:
    print('Invalid')