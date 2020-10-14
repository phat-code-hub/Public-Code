import random
def lottery(nums):
    if num := random.choice(nums):
        return num
    else:
        return "MISS!"
So=[1,2,3,4,5,6,7,8,9]
print(lottery(So))