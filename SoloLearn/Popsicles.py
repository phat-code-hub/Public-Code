siblings = int(input('So kem cho 1 group :').strip())
popsicles=int(input('Tong so kem : ').strip())
pop_num=popsicles//siblings # numbers of popsicle for 3 group = siblings
left=popsicles % siblings
print('give away' if pop_num >=2 and left >= 0 else 'eat them yourself')