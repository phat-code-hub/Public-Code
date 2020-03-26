word =input('words: ').strip()
ans=True
chk=''
while ans:
    for i in range(len(word)):
        chk+=word[i]
        count=word.count(chk)
        if len(chk)==1:
            if count==len(word):
                ans=False
                break
        elif (len(chk) != len(word)):
            if (count*len(chk)) == len(word):
                ans=False
                break
    break
print('prime' if ans else 'not prime')
