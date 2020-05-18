#This program replaces numbers (0-10) written in the sentence 
#into suitale English word
#example:
#input : "Mike buys 3 apples and 4 bananas" (input words are original form (lowercase))
#output : "Mike buys three apples and four bananas"
import re
table={'10':'ten','0':'zero','1':'one','2':'two','3':'three','4':'four',
       '5':'five', '6':'six','7':'seven','8':'eight','9':'nine'}
reg=re.compile(r'(\D)*\d+(\D)*')# have at least one decimal digit
#-----------------------------------------------------------------------
def checkValidString(data):
    return reg.match(data)   
#-----------------------------------------------------------------------
#Main code
try:
    phrase=input('Phrase :').strip().lower()
    assert checkValidString(phrase)
    for n in table.keys():
        phrase=phrase.replace(n,table[n],len(phrase))
    print(phrase)
except:
    print('Phrase was nothing or had not any number!')