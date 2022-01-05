number=int(input('Nhap so: '))
ans=number
count=0
while ans!=1:
    count+=1
    ans0=ans
    if ans % 2 ==0:     
        ans=int (ans0/2)
        print('Step {0}: {1}/2 ={2}'.format(count,ans0,ans))
    else:
        ans=ans0*3+1
        print('Step {0}: {1}*3+1={2}'.format(count,ans0,ans))