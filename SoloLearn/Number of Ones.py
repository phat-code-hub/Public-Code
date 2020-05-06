def tobin(n):
    num=n
    bin=''
    while True:
        bin=str(num % 2)+bin
        num=num // 2
        if num ==0:
            break
    return bin.count('1')
#------------------------------------
try:
    number=int(input('Number: '))
    one_numbers=tobin(number)
    print(one_numbers)
except  :
    print('Invalid!')