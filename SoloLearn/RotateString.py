word=input('String :').strip()
if len(word) ==0:
    print('Nothing!')
elif len(word) ==1:
    print(word)
else:
    print('There are {0} rotated strings of \"{1}\":'.format(len(word),word))
    rot_str=word
    for i in range(len(word)):
        rot_str=rot_str[-1]+rot_str[:len(rot_str)-1]
        print(rot_str)