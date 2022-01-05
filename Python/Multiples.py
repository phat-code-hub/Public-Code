try:
    limit=int(input())
    nums=set(n for n in range(1,limit) if (n % 3 ==0 or n % 5 ==0))
    print(sum(nums))
except :
    print('Invalid number!')

