a = float(input("Введіть a: "))
b = float(input("Введіть b: "))


if a > b:
    X = a / b + 1
elif a == b:
    X = -2
else:  # a < b
    X = (a - b) / a


print("X =", X)
