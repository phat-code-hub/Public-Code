nums = [-1,0,3,5,9,12]
target = 9
# nums = [-1,0,3,5,9,12]
# target = 2
# nums = [-1,0,5]
# target =0

# nums=[5]
# target =5

pos=-1
i,j = 0,len(nums)-1
while i<=j:
    mid  = (i+j)//2
    if nums[mid] ==  target:
        pos= mid
        break
    if nums[mid] > target:
        j = mid-1
    else:
        i = mid+1
    

# i=0;j=len(nums)-1 if len(nums)>1 else 0
# pos = -1
# if target<=nums[j] and target >=nums[i]:
#     while j>=i:
#         if nums[i]== target:
#             pos=i
#             break
#         else:
#             i+=1
#         if nums[j] == target:
#             pos =j
#             break
#         else:
#             j-=1

print(pos)