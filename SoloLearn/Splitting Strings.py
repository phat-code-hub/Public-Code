HYP='-'
ans=''
try:
    word=input('String: ').strip()
    num=int(input('space: '))
    if len(word)==0:
        ans='Nothing'
    elif len(word)==1:
        ans=word
    else:
        if num<=0:
            ans=word
        else:
            if len(word)<=num:
                ans=word
            else:
                s=[]
                for i in range(0,len(word),num):
                    s.append(word[i:i+num])
                ans=HYP.join(s)
    print(ans)
except :
    print('Invalid')