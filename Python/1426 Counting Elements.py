arr = [1,2,3]
arr = [1,1,3,3,5,5,7,7]
set1 = set(arr)
print(set1)
set2 = set([n+1 for n in set1])
print(set2)
print(len(set1 & set2))