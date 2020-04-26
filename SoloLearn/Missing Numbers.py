try:
    limit=int(input('N: '))
    assert limit>0
    num_array=[]
    for i in range(limit):
        s=input('so: ').strip()
        if s!='' and s.isdecimal():
            num_array.append(int(s))
        else:
            break
    num_array=sorted(num_array)
    nums=set(num_array)
    origin={n for n in range(num_array[0],num_array[-1]+1)}
    dif=list(origin-nums)
    differ=list(map(str,dif))
    differ=sorted(differ)
    print(' '.join(differ))
except :
    print('Invalid')