STUDENTS=15
try:
    blue=int(input('blue: '))
    red=int(input('red: '))
    green=int(input('green: '))
    yellow=int(input('yellow: '))
    colors=[blue,red,green,yellow]
    leftovers=[l % STUDENTS for l in colors]
    remain_Blocks=sum(leftovers)
    print(remain_Blocks)
except :
    print('Invalid Color code!')