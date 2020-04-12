FIX_COST=40.00 # Cost for canvas and brushes
TAX=1.1 # 10%
UNIT_PRICE=5.00 #Paint unit price
try:
    color_number=int(input('number: '))
    print(int((FIX_COST+UNIT_PRICE*color_number)*TAX))
except :
    pass