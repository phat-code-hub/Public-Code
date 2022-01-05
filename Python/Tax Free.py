
TAX=1.07 # 7%
try:
    items_prices=input('prices: ').strip().split(',')
    #METHOD 1: directly calculate
    total=0.0
    for price in items_prices:
        if float(price) <20.0:
            total += float(price)*TAX
        else:
            total +=float(price)
    #METHOD 2 : Using builtin functions and reduce 
    # from functools import reduce
    # under20=[float(price) for price in items_prices if float(price)<20.0 ]
    # over20=[float(price) for price in items_prices if float(price)>=20.0 ]
    # total1=reduce(lambda p1,p2: p1+p2,under20)
    # total2=reduce(lambda p1,p2:p1+p2,over20)
    # total=total1*TAX+total2
    print(round(total,2))
except :
    print('Invalid Prices!')

