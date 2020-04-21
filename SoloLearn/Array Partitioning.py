#The Ideas of this solution:
#1)Sort given array descendent
#2)Take first 2 max numbers and add to 2 sub array as delegate ones
#3)If the length of array is even:
#   Adding to subarrays remain items by 2 numbers each, which subarray to be added
#   depend on the difference of two sums of subarrays is small or ot 
# 4)If the length is odd:
#   after step 1 , take the smallest item out for reserve , continue step 2,3 .Then
#   supply this reserve number to subarray who has smaller sum result 

A=[]
B=[]
def Analyse(array):   
    reserved_num=0
    if len(array) % 2 != 0:
        reserved_num=array[-1] # reserverd the smallest item
        data=array[:-1]
    else:
        data=array
    for i in range(0,len(data),2):
        if i==0:
            #add 2 delegate to 2 sub arrays
            A.append(data[0])
            B.append(data[1])
        else:
            #calculate sum and compare for remain numbers
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
    if len(array) % 2 != 0:
        if sum(A)<sum(B):
            A.append(reserved_num)
        else:
            B.append(reserved_num)
    return abs(sum(A)-sum(B))
try:
    size=int(input('Array Size: '))
    array0=input('Array: ').strip().split((','))
    array=[int(n) for n in array0]
    sort_array=sorted(array,reverse=True)
    differ=Analyse(sort_array)
    print(A)
    print(B)
    print(differ)
except :
    print('Invalid info!')