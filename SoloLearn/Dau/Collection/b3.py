ss=[2,3,5,1,8,5,38,3]
a=int(len(ss)/2) #4
b=a*ss[a] #32
print(b)
c=b %(a/2) #0
print(c)
print(a+b+2**c)