l1={"blue","green","blue"}
print(l1)
l2={"green","blue","green"}
print(l2)
l1.add("black")
print(l1)
l3=list((lambda x,y: x-y) (l1,l2))
print(l3[0][2:])
if(2 % 2 == 0):
    print(bool(1))
else:
    print(bool(0))