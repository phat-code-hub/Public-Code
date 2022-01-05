def isAutomorphic(data):
    square_str=str(int(data)**2)
    sub_square=square_str[len(square_str)-len(data):]
    if sub_square == data:
        return True
    else:
        return False
#-----------------------------------------------------------
def findAll(a,b):
    if a>b:
        a,b=b,a
    arr=[]
    for n in range(a, b+1):
        if isAutomorphic(str(n)):
            arr.append(str(n))
    if len(arr)>0:
        print()
        print('From {0} to {1} ,there are {2} automorphic numbers:'.format(a,b,len(arr)))
        print(' '.join(arr))
#-----------------------------------------------------------
#Main Code
try:
    words = input('Number  or range(a,b) for check: ').strip().split(',')
    if len(words) ==1:
        ans='' if isAutomorphic(words[0]) else 'not'
        print('{0} is {1} a automorphic number'.format(words[0],ans))
    else:
        findAll(int(words[0]),int(words[1]))
except :
    print('Invalid Number!')