x=[1,2,3]
def func(x):
    a=42
    x[1]=42
    print(x)
    x=a
    print(x)
func(x)
print(x)