def happyNumber(data):
    if data ==1:
        return True,[1]
    else:
        nums=str(data)
        temp_list=[data]
        repeatSum=0
        while len(nums)>1:
            sums=[int(x)**2 for x in nums]
            repeatSum=sum(sums)
            nums=str(repeatSum)
            temp_list.append(repeatSum)
        if repeatSum==1:
            return True,temp_list
        else:
            return False,temp_list
#-------------------------------------------------------
#1 and 7 are considered special ones so that don't calculate them
def findInRange(down,up):
    found=[]
    if down<=1 and up <7:
        if 1 not in found:
            found.append(1)
    elif down<7 and up >=7:
        if 1 not in found:
            found.append(1)
        if 7 not in found:
            found.append(7)
    for n in range(down,up+1):
        res,ls=happyNumber(n)
        if res:
            if n not in found:
                found.append(n)
    if len(found)>0:
        founds=list(map(str,found))
        print('There are {0} happy numbers from {1} to {2}:'.format(len(found),down,up))
        print(' '.join(founds))
#-------------------------------------------------------
def detailSum(prevSum):
    strData=str(prevSum)
    temp=[]
    for n in strData:
        temp.append(n+' ^ 2')
    return ' + '.join(temp)
#-------------------------------------------------------
def showDetail(sumList):
    if len(sumList)>0 :
        print('{0} is a happy number as:'.format(sumList[0]))
        for item in range(1,len(sumList)):
            detailstr=detailSum(sumList[item-1])
            print('{0} = {1}'.format(detailstr,sumList[item]))
#-------------------------------------------------------
#Main code
print('1-Verify happy number')
print('2-Search happy numbers in range ')
print('3-Show calculation detail')
try:
    opt=int(input('Choose option: '))
    assert 0< opt< 4
    if opt==1: # Check single number
        number=int(input('Number to check:'))
        ans,saved_list=happyNumber(number)
        print()
        print('happy' if ans else 'unhappy,sad!')
    elif opt==2: # check range
        lower=int(input('lower bound:'))
        upper=int(input('upper bound:'))
        print()
        findInRange(lower,upper)
    else: # show sums' details
        number=int(input('Number to check:'))
        if number ==1 or number == 7  :
            print('{0} is considered as a happy number'.format(number))
        else:
            ans,saved_list=happyNumber(number)
            if ans:
                print()
                showDetail(saved_list)
            else:
                print('{0} is not a happy number as repeat sum was {1}'.format(number,saved_list[-1]))
except AssertionError:
    print('Option must be from 1~3') 
except ValueError:
    print('Invalid Value!')