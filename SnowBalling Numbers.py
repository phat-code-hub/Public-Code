def check(data):
    total=data[0]
    chk=[]
    for n in range(1,len(data)):
        chk.append(data[n]>total)
        total+=data[n]
    return all(chk)
try:
    length=int(input('length :'))
    if length>1:
        nums=[]
        for n in range(length):
            num=input('So: ').strip()
            if num.isdecimal():
                nums.append(num)
            else:
                break
        if len(nums)>=length//2:
            print('true' if check(nums) else 'false')
        else:
            print('false')
    else:
        print('false')
except :
    print('Invalid numbers')