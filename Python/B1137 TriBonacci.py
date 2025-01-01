N=12  # N<=37 and N>=0
N=4
TF=[]
TF.append(0)
TF.append(1)
TF.append(1)
for n in range(3,N+1):
    TF.append(TF[n-3]+TF[n-2]+TF[n-1])
print(TF[N])