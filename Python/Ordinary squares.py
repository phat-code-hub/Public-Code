import numpy as np
n,p=[int(x) for x in input().split()]
X=[]
for i in range(n):
    X.append([float(x) for x in input().split()])
y=[float(x)for x in input().split()]
npX=np.matrix(X)
npy=np.matrix(y)
beta=np.array(npy*np.linalg.inv(npX))[0]
print(np.array2string(beta,separator=',',floatmode='unique'))