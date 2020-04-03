number = int(input('Number: '))
test_nums=input('test: ').strip().split()
test= all(number % int(n) == 0 for n in test_nums)
if test:
    print('divisible by all')
else:
    print('not divisible by all')