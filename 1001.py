
n = 7
a = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if i <= j:
            a[i][j] = n - j + i
        else:
            a[i][j] = n - i + j

for r in a:
    print(*r)
