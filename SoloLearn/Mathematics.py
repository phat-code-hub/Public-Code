number=int(input('So :'))
exprs=input('Chuoi :').strip().split()
for i in range(1, len(exprs)):
    index=-1
    value= eval(exprs[i])
    if value == number:
        index=i
        break
if index>=0:
    print('index ', index)