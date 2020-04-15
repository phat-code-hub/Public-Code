from collections import Counter
def checkValidNumber(num_str):
    repeat_list=Counter(num_str)
    isValid=False
    # no repetition for 3 degits number
    if len(num_str) ==3 and len(repeat_list) ==3:
        isValid = True
    # max 2 repetitons for 4 degits number
    if len(num_str) ==4:
        letter_count_list=[lambda n: repeat_list.keys[n] for n in repeat_list]
        print(letter_count_list)
    
checkValidNumber('1411')