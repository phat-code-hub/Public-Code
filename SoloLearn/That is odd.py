max=int(input('Input max number: ').strip())
sum=0
if max >=1:
    list=[]
    for i in range(max):
        str=input('number: ')
        if str != '':
            list.append(int(str))
        else:
            list.append(0)
    for n in list:
        if n % 2 == 0:
            sum += n
print(sum)