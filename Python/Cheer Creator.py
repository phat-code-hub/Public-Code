def sound(yards):
    if yards<1:
        return 'shh'
    elif yards>10:
        return 'High Five'
    else:
        return 'Ra!'*yards
try:
    moved_yard=int(input('Moved yard:'))
    print(sound(moved_yard))
except:
    print('Invalid number!')