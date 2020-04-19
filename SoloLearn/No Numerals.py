#This program replaces numbers (0-9) written in the sentence 
#into suitale English word
#example:
#input : "Mike buys 3 apples and 4 bananas" (input words are original form (lowercase))
#output : "Mike buys three apples and four bananas"
import re
table={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',
        6:'six',7:'seven',8:'eight',9:'nine',10: 'ten'}
reg_null=re.compile(r'.*') #Not null
reg_decimal=re.compile(r'[0-9]+') # have at least one numeric letter
def checkValidString(data):
    return reg_null.match(data) and reg_decimal.search(data)
#-----------------------------------------------------------------------
def convert_Num_toString(wordgroup):
    converted_Sentence=''
    for wd in wordgroup:
        if reg_decimal.search(wd):
            converted_Sentence += table[int(wd)]+' '
        else: #no decimal
            converted_Sentence+=wd.lower()+ ' '
    return converted_Sentence
#-----------------------------------------------------------------------
#Main code
try:
    phrase=input('Phrase :').strip().lower()
    assert checkValidString(phrase)
    words=phrase.split()
    print(convert_Num_toString(words))
except:
    print('Phrase was nothing or had not any number!')