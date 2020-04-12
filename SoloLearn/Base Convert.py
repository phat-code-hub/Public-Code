#Create calculate base set lists
base_set=[chr(i) for i in range(48,58)] # [0-9]
letter_set=[chr(i) for i in range(65,90)] #[A-Z]
#combine two set
base_set.extend(letter_set)
info=input('Number and base: ').strip().split()
try:
    num_str,base_str=info
    num=int(num_str)
    base=int(base_str)
    assert num>=0 and base >=2 and base <=36
    #divided integer and modulus
    converted_number=''
    while num >0:
        div=num // base
        mod= num % base
        converted_number =base_set[mod]+converted_number
        num=div
    print(converted_number)
except:
    print('Number >=0 and  2 <=base <=36')