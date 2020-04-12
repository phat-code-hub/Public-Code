CARROT=7
carrot_num=int(input('carrot: '))
box_num=int(input('box: '))
leftover=carrot_num % box_num
if leftover>=CARROT:
    print('Cake Time')
else:
    print('I need to buy {carrot} more'.format(carrot=CARROT-leftover))