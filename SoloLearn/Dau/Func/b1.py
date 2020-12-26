def func(x):
    for i in range(x):
        yield i**2
print (",".join(list(func(3))))