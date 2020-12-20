y=[]
def loop(x):
    for i in x:
        try:
            y.append(int(i))
        except:
            pass
    return y
z=loop(["2.0","1",y,abs(12j+1)])
print(z)