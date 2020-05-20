import numpy as np
try:
    n,p=[int(x) for x in input().split()]
    data=[]
    for i in range(n):
        datum=input().split()
        assert len(datum) ==p
        data +=datum
    rows_=[float(r) for r in data]
    rows=np.array(rows_).reshape(n,p)
    rows_mean=[round(mean,2) for mean in rows.mean(axis=1)]
    print(rows_mean)
except:
    print('Invallid')