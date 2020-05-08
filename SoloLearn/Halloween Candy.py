try:
    houses=int(input('House visited: '))
    assert houses>=3
    dollar=2
    if houses==4:
        percent=round(dollar/houses*100)
    else:
        if (houses-4) % 3  ==2 :
            dollar+=((houses-4) // 3)*2+2
        percent=round(dollar/houses *100)
    print(percent)
except:
    print('Invalid appropriate integer number')
    print('Visited houses must be more than 2')