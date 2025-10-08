
import math
from module_calc import series_sum

# === Перша частина ===
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
alpha = float(input("Введіть α: "))

if alpha >= 15:
    z = math.sin(2 * a) + math.cos(2 * b)
else:
    z = math.sqrt(a + b**2)

print(f"Результат z = {z:.4f}")

# === Друга частина ===
n = int(input("\nВведіть натуральне число n: "))
result = series_sum(n)
print(f"Результат суми = {result:.4f}")
