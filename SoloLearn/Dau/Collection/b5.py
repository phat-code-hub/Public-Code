def check(x):
    if (x % 3 == 0):
        return False
    return True
a=[i for i in range(6) if check(i)]
print (a)