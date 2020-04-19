#This program replaces numbers (0-9) written in the sentence 
#into suitale English word
#example:
#input : "Mike buys 3 apples and 4 bananas" (input words are original form (lowercase))
#output : "Mike buys three apples and four bananas"
import re
table={'10': 'ten','0':'zero','1':'one','2':'two','3':'three','4':'four',
       '5':'five', '6':'six','7':'seven','8':'eight','9':'nine'}
reg_null=re.compile(r'(.)') #Not null
reg_decimal=re.compile(r'[0-9]+') # have at least one numeric letter
#-----------------------------------------------------------------------
def checkValidString(data):
    return reg_null.match(data) and reg_decimal.search(data)
#-----------------------------------------------------------------------
def Convert_Num_toString(data):
    words=data.split()
    converted_phrase=''
    for w in words:
        if not w.isalpha(): # have decimal letter
            w=str(int(w)) # remove cases like '01'
        for k in table:
            if k in w:
                w=w.replace(k,table[k])
                break
        converted_phrase+=w+ ' '
    return converted_phrase
#-----------------------------------------------------------------------
#Main code
try:
    phrase=input('Phrase :').strip().lower()
    assert checkValidString(phrase)
    print(Convert_Num_toString(phrase))
except:
    print('Phrase was nothing or had not any number!')