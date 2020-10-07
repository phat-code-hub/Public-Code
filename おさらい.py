def fun(*arg):
    i=0
    b=[]
    for val in arg:
        if val ==0:
            # arg[i] =1
            b.append(1)
        else:
            b.append(val)
    
    return b
print(fun(5,2,0,4,0))
