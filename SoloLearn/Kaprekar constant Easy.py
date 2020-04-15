from collections import Counter
def checkNumber(word):
    return len(word)==4 and len(Counter(word))>1
def getResult(str_of_number):
    asc_number=''.join(sorted(str_of_number))
    desc_number=asc_number[::-1]
    return str(int(desc_number)-int(asc_number))
try:
    num_str= input('Four digits number: ')
    assert checkNumber(num_str)
    before_calc=num_str
    after_calc=0
    count=1
    while True:
        after_calc=getResult(before_calc)
        if after_calc == before_calc:
            print('the Kaprekar\'s constant is {0} after {1} repeat times'.format(after_calc,count))
            break
        else:
            count+=1
            before_calc=after_calc
except :
    print('Invalid Number')
    print('number is 4 degits and at least 2 different numbers')