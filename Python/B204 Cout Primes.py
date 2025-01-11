from cmath import sqrt


n=10
if n<=2 : print(0)
else:
    counts = [1] * (n)
    counts[0] = counts[1] =0
    for i in range(2, int(sqrt(n)) + 1):
        if counts[i] == 1:
            for j in range(i * i, n, i):
                counts[j] = 0

    print(sum(counts))