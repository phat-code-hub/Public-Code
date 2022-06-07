import re
import copy
def TakeData():
    nums=""
    while True:
        if nums == "":
            nums = input("Number please  'Enter' for finish:")
        else:
            break
        return nums
        # return re.split("\D",nums.strip())
#-----------------------------------------
def splitData(arr):
    temp=re.split("\D",arr.strip())
    return [int(n) for n in temp]
#-----------------------------------------
def Swap(a,b) : 
    return b,a

#-----------------------------------------
def normalSort(arr):
    count =0
    tail = len(arr)-1
    while tail>0:
        index = 0
        while index < tail:
            count +=1
            if arr[index]> arr[index+1]:
                arr[index],arr[index+1] = Swap(arr[index],arr[index+1])
            index +=1
        tail -=1
    print(f"After normal sorted a={arr} with {count} sorted times")
#-----------------------------------------
def ShakerMethodSort(arr):
    count=0
    top =0 #starting : first element
    tail =len(arr)-1
    while top <tail:
        swap_flag= False
        index = top
        while  index < tail:
            count +=1
            if arr[index] > arr[index+1]:
                arr[index],arr[index+1]=Swap(arr[index],arr[index+1])
                last_index = index
                swap_flag= True
            index +=1
        if swap_flag == False:
            break
        tail = last_index
        swap_flag = False
        index = tail
        while  index > top:
            count +=1
            if arr[index-1] > arr[index]:
                arr[index-1],arr[index]=Swap(arr[index-1],arr[index])
                last_index =index
                swap_flag = True
            index -= 1
        if swap_flag == False:
            break
        top = last_index

    print(f"After Shaken sorted a={arr} with {count} sorted times") 
#-----------------------------------------
def CombMethodSort(arr):
    import random
    arr=list(range(1,101))
    random.shuffle(arr)
    count=0
    top =0 #starting : first element
    tail =len(arr)-1
    #
    gap= len(arr)
    #間隔を挟める割合
    NARROW_RATE =1.3
    swap_flag=False

    while gap >1 or swap_flag ==False:
        gap = int(gap/NARROW_RATE)
        if gap == 0 :
            gap =1
        elif gap == 9 or gap == 10:
            gap = 11
        swap_flag = True
        index =0
        while index + gap <= tail:
            count +=1
            if arr[index] > arr[index+gap]:
                arr[index],arr[index+gap] = Swap(arr[index],arr[index+gap])
                swap_flag =False
            index += 1
    print(f"After Comb sorted a={arr} with {count} sorted times") 

#----Main Code----------
array= TakeData()
a= splitData(array)
print(f"Before a={a}")
normalSort(a)
b =splitData(array)
ShakerMethodSort(b)
c=splitData(array)
CombMethodSort(c)