length=0
def check(data):
    total=data[0]
    chk=[]
    for n in range(1,len(data)):
        chk.append(data[n]>total)
        total+=data[n]
    return all(chk)
try:
    ans=True
    length=int(input('length :'))
    if length>1:
        nums=[]
        for n in range(length):
            num=input('So: ').strip()
            if num.isdecimal():
                nums.append(num)
            else:
                ans=False
                break
        if ans:
            print('true' if check(nums) else 'false')
        else:
            print('false')
    else:
        print('length must be >1')
except :
    print('Invalid numbers')