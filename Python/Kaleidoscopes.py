bought_number=int(input('Bao nhieu '))
if bought_number>=2:
    total=bought_number*5*(1-0.1)
else:
    total=bought_number*5
print('{:.2f}'.format(total*1.07))