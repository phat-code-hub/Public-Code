number=int(input('So :'))
exprs=input('Chuoi :').strip().split()
for i in range(0, len(exprs)):
    value= eval(exprs[i])
    if value == number:
        print('index ', i)
        break