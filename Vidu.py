from itertools import accumulate
acc=accumulate([2*x+1 for x in range(5)])
print (list(acc))