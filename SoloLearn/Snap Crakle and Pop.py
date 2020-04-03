numbers=[]
for i in range(6):
    numbers.append(int(input('so: ')))
sounds=[]
for n in numbers:
    if n % 3 == 0:
        sounds.append('Pop')
    else:
        if n % 2 ==0 :
            sounds.append('Crackle')
        else:
            sounds.append('Snap')
Rice_Sound = ' '.join(sounds)
print(Rice_Sound)