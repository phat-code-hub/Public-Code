def check(n):
    chk=[int(n[i])**(i+1) for i in range(len(n))]
    return sum(chk) == int(n)
#------------------------------------------------------
def checkRange(down,up):
    if down>up:
        down,up=up,down
    return [str(n) for n in range(down,up+1) if check(str(n))]
#------------------------------------------------------
word=input('Number or range (a b):').strip().split()
assert word !='' or len(word)>2
print()
try:
    if len(word)==1:
        print(check(word[0]))
    else:
        lower,upper=word
        isDisariums=checkRange(int(lower),int(upper))
        print('There are {0} disarium numbers from {1} to {2}:'.format(len(isDisariums),lower,upper))
        print(' '.join(isDisariums))
except :
    print('Invalid input info!')
