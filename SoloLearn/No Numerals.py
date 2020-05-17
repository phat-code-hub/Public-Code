#This program replaces numbers (0-10) written in the sentence 
#into suitale English word
#example:
#input : "Mike buys 3 apples and 4 bananas" (input words are original form (lowercase))
#output : "Mike buys three apples and four bananas"
import re
table={'10':'ten','0':'zero','1':'one','2':'two','3':'three','4':'four',
       '5':'five', '6':'six','7':'seven','8':'eight','9':'nine'}
reg=re.compile(r'(\D)*\d+(\D)*')# have at least one decimal digit
reg_num=re.compile(r'\d+')
#-----------------------------------------------------------------------
def checkValidString(data):
    return reg.match(data)   
#-----------------------------------------------------------------------
def replaceNum(num_str):
    numalfa=num_str
    nums=reg_num.findall(numalfa)
    if len(nums)>0:
        for n in nums:
            if int(n)<=10:
                numalfa=numalfa.replace(n,table[n])
    return numalfa
#-----------------------------------------------------------------------
#Main code
try:
    phrase=input('Phrase :').strip().lower()
    assert checkValidString(phrase)
    phrases=phrase.split()
    words=[]
    for wd in phrases:
        temp=wd
        if wd.isalnum():
            temp=replaceNum(wd)
            words.append(temp)
    phrase=(' ').join(words)
    print(phrase)
except:
    print('Phrase was nothing or had not any number!')