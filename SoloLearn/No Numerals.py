#This program replaces numbers (0-9) written in the sentence 
#into suitale English word
#example:
#input : "Mike buys 3 apples and 4 bananas" (input words are original form (lowercase))
#output : "Mike buys three apples and four bananas"
import re
table={'0':'zero','1':'one','2':'two','3':'three','4':'four',
       '5':'five', '6':'six','7':'seven','8':'eight','9':'nine'}
reg_null=re.compile(r'(.)+') #Not null
reg_decimal=re.compile(r'[0-9]+') # have at least one numeric letter
reg_10=re.compile(r'10(?!0)') # Match 10
#-----------------------------------------------------------------------
def checkValidString(data):
    return reg_null.match(data) and reg_decimal.search(data)
#-----------------------------------------------------------------------
def replace_10(datas):
    data=datas
    while True:
        m=reg_10.search(data)
        if m:
            data=data[:m.start()]+'ten'+data[m.end():]
        else:
            break
    return data
#-----------------------------------------------------------------------
#Main code
try:
    phrase=input('Phrase :').strip().lower()
    assert checkValidString(phrase)
    #find 10 number and replace it by 'ten'
    phrase=replace_10(phrase)
    #replace all other numeric words by appropriate term 
    for num in table:
        if num in phrase:
            phrase=phrase.replace(num,table[num],len(phrase))
    print(phrase)
except:
    print('Phrase was nothing or had not any number!')