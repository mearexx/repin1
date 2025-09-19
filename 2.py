N = int(input("Введіть N (1 < N < 9): "))

for i in range(1, N + 1):
    for j in range(N, i - 1, -1):
        print(j, end=" ")
    print()
