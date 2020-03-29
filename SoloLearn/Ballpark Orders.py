TAX=1.07 # 7%
Menus=dict(Nachos=6.0,Pizza=6.0,Cheeseburger=10.0,Water=4.0,Coke=5.0)
#Below is the Same Definition
#Menu={'Nachos':6.0 , 'Pizza':6.00,'Cheeseburger':10.0,'Water':4.0,'Coke':5.0}
prepared_Item=Menus['Coke']
Ordered_Items=input('Menu ').strip().split()
sum=0.0
for item in Ordered_Items:
    if item.capitalize() in  Menus.keys():
        sum += Menus[item.capitalize()]
    else:
        sum += prepared_Item
sum=sum * TAX 
print(sum)