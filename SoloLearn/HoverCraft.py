MAKESHIP_No=10
SALE_PRICE=3000000
INSURANCE=1000000
monthly_cost=2000000*MAKESHIP_No + INSURANCE
cust_Num=int(input('Buy Customer number: '))
Sold_Amount=cust_Num*SALE_PRICE
if Sold_Amount > monthly_cost:
    print('Profit')
elif Sold_Amount == monthly_cost:
    print('Broke Even')
else:
    print('Loss')