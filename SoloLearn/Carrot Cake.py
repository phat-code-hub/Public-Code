CARROT=7
carrot_num=int(input('carrot: '))
box_num=int(input('box: '))
leftover=carrot_num % box_num
if leftover==0:
    need_to_buy=CARROT
else:
    need_to_buy=CARROT-(leftover % CARROT)
if need_to_buy ==0:
    print('Cake Time')
else:
    print('I need to buy {carrot} more'.format(carrot=need_to_buy))