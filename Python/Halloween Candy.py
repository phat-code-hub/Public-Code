import math
try:
    houses=int(input('House visited: '))
    assert houses>=3
    dollar=2
    percent=math.ceil(dollar/houses *100)
    print(percent)
except:
    print('Invalid appropriate integer number')
    print('Visited houses must be more than 2')