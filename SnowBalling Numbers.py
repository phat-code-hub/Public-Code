length=0
def check(data):
    total=data[0]
    chk=[]
    for n in range(1,length):
        chk.append(data[n]>total)
        total+=data[n]
    return all(chk)
try:
    length=int(input('length :'))
    if length>1:
        nums=[]
        for n in range(length):
            nums.append(int(input('So {}:'.format(n+1))))
        print('true' if check(nums) else 'false')
    else:
        print('length must be >1')
except :
    print('Invalid numbers')