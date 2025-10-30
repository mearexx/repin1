t = str(input("Введіть слово: "))

# Перевірка на наявність символу "_"
count_underscore = t.count("_")

if count_underscore > 0:
    print(f"У слові є символи '_' у кількості: {count_underscore}")
else:
    print("У слові немає символів '_'")
