def func(n):
    if (n==1 ) or (n==2):
        return 1
    else:
        return func(n-func(n-1))+func(n-func(n-2))
number= input('So: ')
try:
    if number.isdecimal:
        if int(number)>=0:
            print(func(int(number)))
        else:
            print('Negative number')
except:
    print('Invalid number')
