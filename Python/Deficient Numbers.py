def findFactor(n):
    return [f for f in range(1,n+1) if n % f == 0]
#-------------------------------------------------------------------------------------
def checkOne(num):
    factors=findFactor(num)
    return True if sum(factors)<2*num else False
#-------------------------------------------------------------------------------------
def checkRange(down,up):
    list=[str(n) for n in range(down,up+1) if checkOne(n)]
    print('There are {0} deficient numbers from {1} to {2}:'.format(len(list),down,up))
    print(' '.join(list))
#-------------------------------------------------------------------------------------
def checkDetail(num):
    factors=findFactor(num)
    factors_str=[str(n) for n in factors]
    print('Factors of {0} are :'.format(num))
    print(' '.join(factors_str))
    print('Their sum is ',sum(factors))
    if sum(factors)<2*num:
        ans1='It is a deficient number'
        ans2='<'
    else:
        ans1='It is not a deficient number'
        ans2='>='
    print(ans1)
    print('because it\' sum {0} 2x{1}'.format(ans2,str(num)))
#-------------------------------------------------------------------------------------
#Main code
print('1 - Check deficient number.')
print('2 - Check deficient numbers in range.')
print('3 - Check and show detail.')
try:
    opt=input('Select Option:')
    assert int(opt)<=3
    if opt=='1':
        number=int(input('Number to check: '))
        isDeficient=checkOne(number)
        ans='' if isDeficient else 'not'
        print('{0} is {1} deficient number'.format(str(number),ans))
    elif opt=='2':
        down_limit=int(input('lower bound: '))
        up_limit=int(input('upper bound: '))
        checkRange(down_limit,up_limit)
    else:
        number=int(input('Number to check detail: '))
        checkDetail(number)
except :
    print('Option must be <=3')
