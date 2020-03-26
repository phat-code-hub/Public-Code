import re
# them=list(lambda l: chr(l) for l in range(97,123))
# CHARACTER=[]#[lambda x: chr(x) for x in range(97,123)]
CHARACTER=[]
for i in range(97,123):
    CHARACTER.append(chr(i))
print(CHARACTER)
# CHARACTER=('a','b','c','d','e','f', \
#     'g','h','i','j','k','l', \
#     'm','n','o','p','q','r', \
#     's','t','u','v','w','x','y','z')
len=len(CHARACTER)  
reg=re.compile('([a-zA-Z ])+')
str=input('string: ').strip().lower()
m=reg.match(str)
if m:
    ans=[]
    for w in str:
        if w in CHARACTER:
            index=CHARACTER.index(w)
            ans.append(CHARACTER[index*(-1)-1])
        elif w == ' ':
            ans.append(w)
        else :
            pass
    answer=''.join(ans)
    answer.strip()
    print(answer)
else:
    print('Invalid sentence!')