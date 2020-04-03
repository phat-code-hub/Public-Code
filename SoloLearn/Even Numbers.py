numbers=input('chuoi so: ').split()
list=[n for n in numbers if int(n) % 2 ==0]
print(' '.join(list))