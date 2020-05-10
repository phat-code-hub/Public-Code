import numpy as np
mat=None
#-------------------------------------------------
def initMatrix(limit):
    mat0=[]
    mat_=[]
    temp_=[]
    for n in range(limit):
        temp_=input('Row {0}: '.format(n+1)).split()
        mat_=[int(x) for x in temp_ ]
        mat0.append(mat_)
    return np.array(mat0)
#-------------------------------------------------
def rorateMatrix(data):
    print('Origin Matrix =')
    print(data)
    print('Rotate 90 degrees: ')
    print(np.rot90(data,3))
    print('Rotate 270 degrees: ')
    print(np.rot90(data,1))
#-------------------------------------------------
#Main Code
try:
    size=int(input('Size of matrix N= '))
    mat=initMatrix(size)
    assert mat.shape[0]==mat.shape[1]
    rorateMatrix(mat)
except:
    print('Invalid square matrix!')