try:
    houses=int(input('House visited: '))
    assert houses>=3
    mod=houses % 3
    div= houses //3
    # the same code :div,mod=divmod(houses,3)
    if mod ==2: # gift may be dollar bills 
        dollar_Case=div*2+2
    else: # toothbrushes only
        dollar_Case=div*2
    percentage=round((dollar_Case/houses)*100)
    print(percentage)
except:
    print('Invalid appropriate integer number')