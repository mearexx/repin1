# Введення кількості елементів масиву
n = int(input("Введіть кількість елементів масиву (N): "))

# Введення елементів масиву (дійсні числа)
print(f"Введіть {n} дійсних чисел:")
arr = [float(input()) for _ in range(n)]

print("Введений масив:", arr)

# Вибір додатних елементів
positive_elements = [x for x in arr if x > 0]

# Перевірка, чи є додатні елементи
if len(positive_elements) > 0:
    avg = sum(positive_elements) / len(positive_elements)
    print("Середнє арифметичне додатних елементів:", avg)
else:
    print("У масиві немає додатних елементів.")
