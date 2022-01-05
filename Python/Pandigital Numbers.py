from collections import Counter
def isValid(data):
    return data.isdecimal()and data[0]!='0'
def checkPandigital(word):
    count=Counter(word)
    if len(count)==10:
        print('{0} is pandigital'.format(word))
        print('The frequency of each appeared digits are:')
        for i in range(10):
            print('{0} : {1} times'.format(str(i),count[str(i)]))
    else:
        print('{0} is not pandigital'.format(word))
try:
    num_str=input('Number: ').strip()
    assert isValid(num_str)
    checkPandigital(num_str)
except:
    print('Invalid number!')