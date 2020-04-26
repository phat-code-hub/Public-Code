import numpy as np
array=[]
def check(data):
    global array
    dat=data
    array=analyse(dat)
    sums=[sum(a) for a in array]
    sub=[n-sums[0]== 0 for n in sums]
    return all(sub),sums[0]
def analyse(darray):
    array_list=darray
    arr=np.array(darray)
    for i in range(arr.shape[0]):
        array_list.append(list(arr[:,i]))
    dia1=list(arr.diagonal())
    dia2=list((np.rot90(arr)).diagonal())
    array_list.append(dia1)
    array_list.append(dia2)
    return array_list
def divideArray(code):
    global array
    if code<3:
        pass
    else:
        pass
def show(res,sums):
    global array
    if answer:
        print('It is a magic square with the magic sum {0}'.format(sums))
        for i in range(2):
            ans1,ans2,ans3,name=divideArray(i)

    else:
        print('it is not a magic square.')
nums=[]
try:
    num_str=[]
    print('input arrays (blank for finish): ')
    while True:
        array=input('array: ').strip()
        if array == '':
            break
        else:
            num_str=array.split()
            num0=list(map(int,num_str))
            nums.append(num0)
    answer,total=check(nums)
    show(answer,total)
except :
    print('Invalid Number!')