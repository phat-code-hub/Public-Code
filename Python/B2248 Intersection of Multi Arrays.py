"""
    Given a 2D array nums that contains n arrays of distinct integers, 
    return a sorted array containing all the numbers that appear in all n arrays.

    For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 
    3 and 4 are the only numbers that are in all arrays.
    
    Created by Ueda
"""
from collections import defaultdict


nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
#Create dcitionary for counting existing times 
counts = defaultdict(int)

for num in nums:
    for n in num:
        counts[n] +=1
    
n =len(nums)
#Create list of result
res =[]

for key in counts:
    if counts[key] == n:
        res.append(key)

res.sort()
print(res,*res)