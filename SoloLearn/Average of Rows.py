import numpy as np
try:
    n,p=[int(x) for x in input().split()]
    data=[]
    for i in range(n):
        datum=input().split()
        assert len(datum) ==p
        data +=datum
    print(data)
    rows_=[float(r) for r in data]
    rows=np.array(rows_).reshape(n,p)
    print(rows.mean(axis=1))
except:
    print('Invallid')