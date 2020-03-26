from functools import reduce
from operator import add
TAX=1.07
DISCOUNT=0.3
items_prices=input('Items:').strip().split(',')
prices_Before_Discount=[float(n) for n in items_prices]
#search max price
max_price=max(prices_Before_Discount)
prices_After_Discount=[]
for price in prices_Before_Discount:
    if price == max_price:
        #remain price for max item
        discounted_price=price
    else:
        #Other prices are discounted 30%
        discounted_price=price*(1-DISCOUNT)
    prices_After_Discount.append(discounted_price)
#use operator add for reduce
total_Without_Discount=reduce(add,prices_Before_Discount)
#use lambda for reduce
total_Discount=reduce(lambda v1,v2: v1+v2,prices_After_Discount)
saved_money=int(TAX*(total_Without_Discount-total_Discount))
print(saved_money)