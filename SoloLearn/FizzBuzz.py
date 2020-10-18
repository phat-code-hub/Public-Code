n=int(input())
for x in range(1,n):
    if (x %2):
        if (x % 3 == 0 and x % 5 == 0 ):
            print("SoloLearn")
        elif( x % 3 == 0):
            print("Solo")
        else:
            print("Learn")
    else:
        continue
