import string
word=input('word: ').strip()
camel=''
for i in range(len(word)):
    mid=word[i]
    if mid in string.ascii_uppercase:
        if i==0:
            camel += mid.lower()
        else:
            camel+='_'+mid.lower()
    else:
        camel+=mid
print(camel)