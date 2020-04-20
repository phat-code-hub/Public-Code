Q_list=[1,1]
def func(n):
    n_1=n-Q_list[n-2]
    n_2=n-Q_list[n-3]
    return Q_list[n_1-1]+Q_list[n_2-1]
#------------------------------------------------
number_str= input('So: ')
try:
    number=int(number_str)
    assert number>=3
        res=func(i)
        Q_list.append(res)
    # print(Q_list)
    print(Q_list[-1])
except:
    print('Invalid number')
