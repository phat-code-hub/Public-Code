try:
    houses=int(input('House visited: '))
    assert houses>=3
    if houses==3: # 3:do not give candy, 4: give candy, toothbrushes and dollar
        dollar_Case=2
    else: # > 4
        dollar_Case=2
        # mod=houses % 4
        # div= houses //4
        # # the same code :div,mod=divmod(houses,3)
        # if mod==3: # can give dollar
        #     dollar_Case=div*2+2
        # else:
        #     dollar_Case=div*2
    percentage=round((dollar_Case/houses)*100)
    print(percentage)
except:
    print('Invalid appropriate integer number')
    print('Visited houses must be more than 2')