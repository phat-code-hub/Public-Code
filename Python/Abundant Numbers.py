factors=[]
def init(N):
    global factors
    for i in range(1,N+1):
        factors=[x for x in range(1,N+1)]
#-----------------------------------------------------
def isAbundant(num,isRange=False):
    global factors
    init(num)
    factors_List=[n for n in factors if num % n == 0]
    factors_str=list(map(str,factors_List))
    factors_show_list=', '.join(factors_str)
    factors_show_sum=' + '.join(factors_str)
    factors_sum=sum(factors_List)
    if not isRange:
        if factors_sum> 2*num:
            return True,factors_show_list,factors_show_sum,factors_sum
        else:
            return False,factors_show_list,factors_show_sum,factors_sum
    else:
        if factors_sum> 2*num:
            return True
        else:
            return False
#-----------------------------------------------------
def findRange(down,up):
    if down>up:
        down,up=up,down
    init(up)    
    list_up=[str(n) for n in range (down, up+1) if isAbundant(n,True)]
    if len(list_up)>0:
        print('There are {0} abundant numbers from {1} to {2}:'.format(len(list_up),down,up))
        print(' '.join(list_up))
    else:
        print('There is no abundant number from {0} to {1}'.format(down,up))
#-----------------------------------------------------
#Main Code
print('1 - Check abundant number.')
print('2 - Check abundantt numbers in range.')
print('3 - Check and show detail.')
try:
    opt=int(input('Select Option: '))
    assert int(opt)<=3
    if opt != 2:
        number=int(input('Check number: '))
        print()
        ans,play_list1,play_list2,play_sum=isAbundant(number)
        if ans:
            print('{0} is an abundant number'.format(number))
            if opt == 3:
                print('Factors of {0} are {1}'.format(number,play_list1))
                print('Sum is {0} = {1} > 2 * {2}'.format(play_list2,play_sum,number))
        else:
            print('{0} is not an abundant number'.format(number))
    else:
        lower =int(input('lower bound: '))
        upper=int(input('upper bound: '))
        print()
        findRange(lower,upper)
except :
    print('Invalid')