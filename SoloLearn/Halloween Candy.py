try:
    houses=int(input('House visited: '))
    assert houses>=3
    dollar=2
    if houses==3:
        percent=0
    elif houses==4:
        percent=50
    else:
        le=houses //10
        chia=(houses -4) % 3
        if chia  ==2 :
            dollar+=chia*le
        percent=round(dollar/houses *100)
    print(percent)
except:
    print('Invalid appropriate integer number')
    print('Visited houses must be more than 2')