import random
import datetime
ALP_=[chr(n) for n in range(65,91)]
ALP=''.join(ALP_)
r=random.choice(ALP)
alp=''
for c in ALP:
    if c != r:
        alp +=c
print(alp)
st=datetime.datetime.now()
ans=input('The missing character in the list is: ').upper()
if ans==r:
    print('Right Answer!')
    et=datetime.datetime.now()
    print(f'You spent {(et-st).seconds}s')
else:
    print ('Incorrect!')