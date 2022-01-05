from sympy import sieve
limit=[]
def check(num):
    global limit
    div=[d for d in limit if num % d == 0]
    div_2=[v**2 for v in div]
    chk=[num % n ==0 for n in div_2]
    if any(chk):
        ans='true'
    else:
        ans='false'
    print('{0} : {1} '.format(num,ans))
def checkRange(down,up):
    for m in range(down,up):
        check(m)
try:
    infos=input('Number or range(a b): ').strip().split()
    if len(infos)==1:
        up=int(infos[0])+1
    else:
        down=int(infos[0])
        up=int(infos[-1])+1
    limit=[n for n in sieve.primerange(2,up)]
    if len(infos)==1:
        check(int(infos[0]))
    else:
        checkRange(down,up)
    
except :
    print('Invalid Number!')