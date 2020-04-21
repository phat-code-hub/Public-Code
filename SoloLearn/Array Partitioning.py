ls0=[2,5,4,40,7,15,20,25]
A=[]
B=[]
ls=sorted(ls0,reverse=True)
rev=sorted(ls0)
def Analyse(data):
    if len(data) % 2 == 0:
        A.append(data[0])
        B.append(data[1])
        for i in range(2,len(data),2):
            anum=data[i]
            bnum=data[i+1]
            sum1=sum(A)+anum
            sum2=sum(B)+bnum
            sum_sub1=abs(sum1-sum2)
            sum3=sum(A)+bnum
            sum4=sum(B)+anum
            sum_sub2=abs(sum3-sum4)
            if sum_sub1<=sum_sub2:
                A.append(anum)
                B.append(bnum)
            else:
                A.append(bnum)
                B.append(anum)
    else:
        pass
    # return abs(sum(A)-sum(B))
print(ls)
Analyse(ls)
print(A)
print(B)
print(sum(A))
print(sum(B))
print(abs(sum(B)-sum(A)))