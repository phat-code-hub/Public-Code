ls0=[2,5,4,7,15,20]
A=[]
B=[]
ls=sorted(ls0,reverse=True)
rev=sorted(ls0)
print(ls)
print(rev)
for i in range(0,len(ls),2):
    A.append(ls[i])
    B.append(ls[i+1])
print(A)
print(B)
print(sum(A))
print(sum(B))