from collections import Counter
def checkNumber(word):
    return len(word)==4 and len(Counter(word))>1
def getResult(str_of_number,step_count):
    asc_number=''.join(sorted(str_of_number))
    desc_number=asc_number[::-1]
    result= int(desc_number)-int(asc_number)
    print('Step {0} : {1} - {2} = {3}'.format(step_count,desc_number,asc_number,result))
    return str(result)
try:
    num_str= input('Four digits number: ')
    assert checkNumber(num_str)
    print()
    print('n=',num_str)
    print()
    before_calc=num_str
    after_calc=0
    count=1
    while True:
        after_calc=getResult(before_calc,count)
        if after_calc == before_calc:
            print()
            print('After {1} steps ,the Kaprekar\'s constant is converged to {0}.'.format(after_calc,count))
            break
        else:
            count+=1
            before_calc=after_calc
except :
    print('Invalid Number')
    print('number is 4 degits and at least 2 different numbers')