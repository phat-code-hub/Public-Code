try:
    percent=0.0
    visited_house=int(input('House visited: '))
    assert visited_house>3
    mod=visited_house % 3
    div= visited_house //3
    # the same code :div,mod=divmod(visited_house,3)
    if mod ==2: # gift may be dollar bills 
        dollar_Case=div*2+2
    else: # toothbrushes only
        dollar_Case=div*2
    percentage=round(dollar_Case/visited_house*100)
    print(percentage)
except:
    print('Invalid appropriate integer number')