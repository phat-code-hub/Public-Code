#This program replaces numbers (0-10) written in the sentence 
#into suitable English word
#example:
#input : "Mike buys 3 apples and 4 bananas" (input words are original form (lowercase))
#output : "Mike buys three apples and four bananas"
import re
table={'10':'ten','0':'zero','1':'one','2':'two','3':'three','4':'four',
       '5':'five', '6':'six','7':'seven','8':'eight','9':'nine'}
#-----------------------------------------------------------------------
#Main code
text=input().strip().lower()
newText =text
idx = 0
for k in table.keys():
    idx = newText.find(k,max(idx,0))
    while idx >= 0:
        newText= newText.replace(k,table[k])
        idx = newText.find(k,idx)
print(newText)