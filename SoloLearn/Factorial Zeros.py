MAX_LIMIT=10
count=0
#--------------------------------------------------------
#Cut result in case of it's lenghth over LIMIT to avoid overflow if any
#Can increase limit if the number is too big
def cut(num):
    if len(str(num)) >MAX_LIMIT:
        num=int(str(num)[len(str(num))-MAX_LIMIT:])
    return num
#--------------------------------------------------------
def count_0(n,num):
    global count
    res=num
    if n % 10 ==0:
        res*=(n // 10)
        count+=1
    else:
        res*=n
        if res % 10 ==0:
            res=res//10
            count+=1
    return cut(res)
#--------------------------------------------------------
def Analyse(n):
    ans=1
    print('Calcucalting...')
    for i in range(n,1,-1):
        ans=count_0(i,ans)
        #comment out to check
        #print('Answer x {0} = {1}'.format(i,ans))
#--------------------------------------------------------
#Main Code
try:
    num=int(input('Number: '))
    assert num>=0
    Analyse(num)
    print('{0}! has {1} trailing zeros'.format(num,count))
except:
    print('Number is not positive integer!')