feet=42
DAY=7
NIGHT=2
days=1
KQ=0
while(True):
    if ((KQ+DAY) >=feet):
        KQ0=KQ
        KQ += DAY
        print("Day {0}:{1}+{2}={3}".format(days,KQ0,DAY,KQ))
        print(days)
        break
    else:
        KQ0=KQ
        KQ += (DAY-NIGHT) #+5
        if (KQ0>0):
            print("Day {0}:{1}+{2}-{3}={4}".format(days,KQ0,DAY,NIGHT,KQ))
        else:
            print("Day {0}:{1}-{2}={3}".format(days,DAY,NIGHT,KQ))
        days+=1