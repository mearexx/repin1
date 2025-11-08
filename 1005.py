
students = {
    "Ivan_Petrenko": [12, 10, 9, 10, 5, 7, 8, 5, 12, 10, 8, 10],
    "Olha_Shevchenko": [12, 10, 9, 5, 6, 7, 4, 3, 12, 4, 10, 9],
    "Serhii_Melnyk": [12, 3, 4, 6, 5, 5, 3, 7, 5, 4, 8, 9],
    "Kateryna_Bondar": [12, 4, 10, 7, 5, 8, 3, 5, 7, 8, 6, 7],
    "Andrii_Koval": [10, 10, 9, 10, 8, 7, 12, 9, 10, 10, 9, 11],
    "Yuliia_Havrylko": [5, 6, 7, 5, 4, 7, 5, 4, 4, 8, 7, 6],
    "Maksym_Sydorenko": [7, 8, 5, 8, 8, 9, 8, 7, 7, 10, 8, 8],
    "Nazar_Khomenko": [6, 7, 8, 9, 10, 10, 9, 7, 8, 9, 10, 9],
    "Alina_Tkach": [2, 3, 5, 4, 5, 4, 3, 3, 5, 8, 5, 6],
    "Sofiia_Lytvyn": [12, 12, 12, 10, 10, 9, 8, 9, 9, 8, 9, 9]
}

# Функція для обчислення середніх балів
def average_grades(students):
    averages = {}
    for name, grades in students.items():
        averages[name] = sum(grades) / len(grades)
    return averages

# Функція для обчислення середнього по класу
def class_average(averages):
    return sum(averages.values()) / len(averages)

# Функція для виведення результатів
def print_results(averages, class_avg):
    print(f"Середня оцінка по класу: {class_avg:.2f}\n")
    print("Учні, у яких середня оцінка вище середньої по класу:")
    for name, avg in averages.items():
        if avg > class_avg:
            print(f"{name}: {avg:.2f}")

# Основна програма
averages = average_grades(students)
class_avg = class_average(averages)
print_results(averages, class_avg)
