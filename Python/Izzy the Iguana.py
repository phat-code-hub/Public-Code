ENOUGH_POINT=10
snack_points={'Lettuce':5,'Carrot':4,'Mango':9,'Cheeseburger':0}
snacks=input('Total snack: ').strip().split()
sum=0
if len(snacks) >0:
    for snack in snacks:
        sum += snack_points[snack.capitalize()]
print('Come on Down!' if sum>=ENOUGH_POINT else 'Time to wait')