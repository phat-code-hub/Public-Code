num=int (input())
def fibonacci(n):
    if (n+1) == 1:
        return 0
    elif (n+1) == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(num):
    print(fibonacci(i))