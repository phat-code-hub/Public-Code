from collections import Counter
def checkValidNumber(num_str):
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
num =input('input any number in range(101 ~ 9999): ' ).strip()
print(checkValidNumber(num))