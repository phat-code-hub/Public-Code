total_Eggs=int(input('total:'))
myself_basket=int(input('myself :'))
friends_basket=int(input('friends:'))
all_found_out= total_Eggs == myself_basket+friends_basket
if all_found_out:
    print('Candy Time')
else:
    print('Keep Hunting')