try:
    houses=int(input('House visited: '))
    assert houses>=3
    if houses==3: # 3:do not give candy, 4: give candy, toothbrushes and dollar
        dollar_Case=0
    else:
        dollar_Case=2
    percentage=round((dollar_Case/houses)*100)
    print(percentage)
except:
    print('Invalid appropriate integer number')
    print('Visited houses must be more than 2')