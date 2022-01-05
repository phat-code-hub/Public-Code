try:
    names=[]
    limit=int(input('so:'))
    for i in range(limit):
        w=input('word: ').strip()
        if len(w)>0:
            names.append(w)
        else:
            break
    Initials=[]
    for name in names:
        spl=name.split()
        fisrt=[l[0] for l in spl]
        Initials.append(''.join(fisrt))
    print(' '.join(Initials))
except :
    print('Invalid info!')
