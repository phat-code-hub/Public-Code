# Pig Latin is a program that convert the same origin words in the same order word
# except the first letter of each origin words will be put into it's end and 
# then add "ay" at the end of each converted words finally.
#Input : String that is normal english sentence (don't accept punctuation and captitalization)
#Output : A string of the same sentence in Pig Latin
# Example : 
# input : " Xthis&& Yis ZMike's Sbread%% "
# output : "thisxay isyay mikezay breadsay" 
from string import punctuation
SUFFIX='ay'
str=input('Any string: ').strip()
#remove capital letter
str=str.lower()
#remove punctuation character
sentence0=''
for w in str:
    if not w in punctuation:
        sentence0 += w
sentences=sentence0.split()
if len(sentences) >1 : # 1 word sentence
    p=[]
    ch=''

    for w in sentences:
       ch=w[1:]+w[:1]+SUFFIX
       p.append(ch)
    pig_Latin=' '.join(p)
else: # more word sentence
    w = sentences[0][1:]+sentences[0][:1]+SUFFIX
    pig_Latin=''.join(w)
print(pig_Latin)