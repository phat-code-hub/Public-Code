n= int(input("So chieu matran: "))
ans = [[0] * n for _ in range(n)]
cnt = 1
for loop in range((n + 1) // 2):
    # direction 1 - traverse from left to right
    for i in range(loop, n - loop):
        ans[loop][i] = cnt
        cnt += 1
    # # direction 2 - traverse from top to bottom
    for i in range(loop + 1, n - loop):
        ans[i][n - loop - 1] = cnt
        cnt += 1
    # # direction 3 - traverse from right to left
    for i in range(n - loop - 2, loop - 1, -1):
        ans[n - loop - 1][i] = cnt
        cnt += 1
    # # direction 4 - traverse from bottom to top
    for i in range(n - loop - 2, loop, -1):
        ans[i][loop] = cnt
        cnt += 1
    
for i in range(n):
    print(ans[i])