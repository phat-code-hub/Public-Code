import math
from string import punctuation
str=input("Sentence: ").strip()
word0=str.split()
words=[]
for w in word0:
    wd=''
    for ch in w:
        if ch not in punctuation:
           wd += ch
    words.append(wd)
lens= 0
for w in words:
    lens += len(w)
print(math.ceil(lens/len(words)))