import numpy as np
array=[]
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
def check(data):
    global array
    dat=data
    array=analyse(dat)
    sums=[sum(a) for a in array]
    sub=[n-sums[0]== 0 for n in sums]
    return all(sub),sums[0]

def divideArray(code):
    global array
    size=(len(array)-2)//2
    matrix_attr=['Rows','Columns','Diagonals']
    arrs=[]
    if code==0:
        down=0
        up=size
    elif code == 1:
        down=size
        up=size*2
    else:
        down=size*2
        up=size*2+2
    attr_name=matrix_attr[code]
    for n in range(down,up):
        arr=list(map(str,array[n]))
        arrs.append(' + '.join(arr))
    res=' = '.join(arrs)
    return res,attr_name
def show(res,sums):
    global array
    if answer:
        print('It is a magic square with the magic sum {0}'.format(sums))
        for i in range(3):
            expr,name=divideArray(i)
            print('{0} = {1} ({2}) '.format(expr,sums,name))
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