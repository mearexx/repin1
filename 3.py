
def expression(n):
    s = 0
    for i in range(1, n + 1):
        s += (i + 1) / i
    z = (1.1) * s
    return z

# Основна програма
n = int(input("Введіть натуральне число n: "))

while n <= 0:
    n = int(input("Число має бути натуральним (більше 0). Введіть ще раз n: "))

print("Результат обчислення виразу z = ", expression(n))
