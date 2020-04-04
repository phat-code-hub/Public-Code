RATE=1.1
items_price=input('Price: ').strip().split()
EU_Price=[float(n) for n in items_price]
max=max(EU_Price)
if max*RATE <= 20:
    print('On to the terminal')
else:
    print('Back to the store')