ENOUGH_POINT=10
snack_points={'Lettuce':5,'Carrot':4,'Mango':9,'Cheeseburger':0}
print(snack_points['Cheeseburger'])
snacks=input('Total snack: ').strip().split()
sum=0
for snack in snacks:
    sum += snack_points[snack]
print(sum)
print('Come on Down' if sum>=ENOUGH_POINT else 'Time to wait')