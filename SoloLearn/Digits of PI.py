def calculate(n):
    tich=4/(8*n+1)-2/(8*n+4)-1/(8*n+5)-1/(8*n+6)
    ans=16**(-n) * tich
    return ans
def pidigit(n):
    res=0
    for i in range(n):
        res+=calculate(i)
    return str(res)
so=5
hso=pidigit(so)
print(hso)
