#This program replaces numbers (0-9) written in the sentence 
#into suitale English word
#example:
#input : "Mike buys 3 apples and 4 bananas" (input words are original form (lowercase))
#output : "Mike buys three apples and four bananas"
import re
from string import punctuation
table={
    0:'zero',
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine'
}
# reg=re.compile(r'([a-zA-Z0-9 ])+')
reg=re.compile(r'(\d|\w|\s)+')
reg_num=re.compile(r'[0-9]')
cau=input('iput sentence : ').strip()
ch=''
for w in cau:
    if not w in punctuation:
        ch += w
    else:
        ch=''     
        break
if len(ch)>0:
    temp=[]
    index=0
    words=ch.lower().split()
    for wd in words:
        index +=1
        if wd.isdecimal():
            letter= table[int(wd)]
            if index==1:
                letter=letter.capitalize()
            temp.append(letter)
        else:
            temp.append(wd)
    no_Numeral=' '.join(temp)
    print(no_Numeral)
else:
    print('Invalid sentence')
