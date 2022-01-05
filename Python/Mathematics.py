number=int(input('So :'))
exprs=input('Chuoi :').strip().split()
ans=-1
for i in range(0, len(exprs)):
    value= eval(exprs[i])
    if value == number:
        ans=i
        break
if ans >=0:
    print('index',ans)
else:
    print('none')