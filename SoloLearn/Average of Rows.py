import numpy as np
try:
    # dim=input('Dimension: ').split()
    dim=input().split()
    n,p=dim
    data=[]
    for i in range(int(n)):
        # datum=input('Row {}:'.format(i+1)).split()
        datum=input().split()
        assert len(datum) ==int(p)
        data +=datum
    rows_=[float(r) for r in data]
    rows=np.array(rows_).reshape(int(n),int(p))
    print(rows.mean(axis=1))
except:
    print('Invallid')