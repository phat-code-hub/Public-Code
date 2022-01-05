from collections import Counter
#-----------------------------------------------------------------------------------------
def checkValid(num_str):
    repeat_list=Counter(num_str)
    isValid=False
    # no repetition for 3 degits number
    if len(num_str) ==3 and len(repeat_list) ==3:
        # len(repeat_list) ==3  means no repeat
        isValid = True
    # max 2 repetitons for 4 degits number
    if len(num_str) ==4:
        # There are five cases of Counter values:
        # 4 : 4 digits are same : too repeat
        # (3,1) : 3 digits are same : too repeat
        # (2,2) : 2 repeats
        #(2,1,1) : 1 repeat
        #  (1,1,1,1) : no repeat 
        if max(repeat_list.values()) ==2 or len(repeat_list)==4:
            isValid=True
    return isValid
#-----------------------------------------------------------------------------------------
def calculate(str_of_number,step_count):
    asc_num=''.join(sorted(str_of_number))
    desc_num=asc_num[::-1]
    result= int(desc_num)-int(asc_num)
    print('Step {0} : {1} - {2} = {3}'.format(step_count,desc_num,asc_num,result))
    return str(result)
#-----------------------------------------------------------------------------------------
try:
    num_str =input('input any number in range(101 ~ 9999): ' ).strip()
    assert int(num_str)>100 and int(num_str)<10000
    if checkValid(num_str) :
        before=num_str
        after=0
        step=1
        print()
        while True:
            after=calculate(before,step)
            if after == before:
                print()
                print('After {0} steps ,the Kaprekar\'s constant of {1} approached {2}.'.format(step,num_str,after))
                break
            else:
                step+=1
                before=after
    else:
        print('This  number is too repeatitons')
except :
    print('Invalid number')