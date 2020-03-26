from functools import  reduce
#Validate Credit card number by Luhn method
#1) The Length of number must be 16
#2) Reverse number
#3) Multiple every second digit by 2
#4)Subtract 9 from all numbers that higher than 9
#5)Add all digits together
#6)Modulo 10 of that sum should be equals to 0 

card_number=input('card :').strip()
result='valid'
if len(card_number)!=16:
    result='not valid'
else:
    card_rev=card_number[::-1]
    groups=[]
    for i in  range(0,16,2):
        groups.append(int(card_rev[i]))
        num=int(card_rev[i+1])*2
        if num >9 :
            num-=9
        groups.append(num)
    total= reduce(lambda n1,n2: n1+n2,groups)
    if total % 10 !=0 :
        result=False
print(result)