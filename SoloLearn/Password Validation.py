SPECIAL_LETTER='!@#$%&*'
LENGTH=7
pwd=input('PassWord please: ').strip()
len= len(pwd)>=LENGTH
if len:
    decimal_count=0
    special_letter_count=0
    for w in pwd:
        if w.isdecimal():
            decimal_count += 1
        elif w in SPECIAL_LETTER:
            special_letter_count +=1
        else:
            pass
    if decimal_count >=2 and special_letter_count>=2:
        print('Strong')
    else:
        print('Weak')
else:
    print('Weak')