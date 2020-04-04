def func(n):
    if (n==1 ) or (n==2):
        return 1
    else:
        return func(n-func(n-1))+func(n-func(n-2))
#------------------------------------------------
number_str= input('So: ')
try:
    number=int(number_str)
    if number <=0:
        print('Not positive integer!')
    elif number==1 or number==2:
        print(1)
    else :
        print(func(int(number))) 
except:
    print('Invalid number')
