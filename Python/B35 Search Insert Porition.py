nums = [1,3,5,6]
# nums = [1,3,5,6,8,9,9,9]
target = 1
pos=0
i=0 ; j= len(nums)
if target<=nums[0]:
    pos=0
elif target>nums[j-1]:
    pos=j
else:
    while j>=i+1:
        if nums[j-1]>=target:
            j -=1
        else:
            pos=j
            break
print(pos)