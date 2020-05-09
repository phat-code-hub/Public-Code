#This program replaces numbers (0-10) written in the sentence 
#into suitale English word
#example:
#input : "Mike buys 3 apples and 4 bananas" (input words are original form (lowercase))
#output : "Mike buys three apples and four bananas"
import re
table={'10':'ten','0':'zero','1':'one','2':'two','3':'three','4':'four',
       '5':'five', '6':'six','7':'seven','8':'eight','9':'nine'}
reg_null=re.compile(r'(.)+') #Not null
reg_decimal=re.compile(r'[0-9]+') # have at least one numeric letter
reg_num=re.compile(r'(\d)+')
#-----------------------------------------------------------------------
def checkValidString(data):
    return reg_null.match(data) and reg_decimal.search(data)
#-----------------------------------------------------------------------
def extract(st):
    a=[]
    b=''
    for i in st:
        if i.isdecimal():
            b+=i
        else:
            if len(b)>0:
                if int(b)<=10:
                    a.append(table[str(int(b))])
                else:
                    a.append(b)
            b=''
            a.append(i)
    return ''.join(a)   
#-----------------------------------------------------------------------
#Main code
try:
    phrase=input('Phrase :').strip().lower()
    assert checkValidString(phrase)
    phrases=phrase.split()
    mang=[]
    for w in phrases:
        l=w
        if reg_num.search(w):
            if w.isnumeric():
                if int(w) <=10:
                    l=table[str(int(w))]
                else:
                    l=w
            else:
                l=extract(w)
        mang.append(l)
    phrase=' '.join(mang)
    print(phrase)
except:
    print('Phrase was nothing or had not any number!')