import json

# початкові дані про учнів
students = [
    {"Surname": "Коваль", "Grades": [9, 8, 10, 7, 9]},
    {"Surname": "Іваненко", "Grades": [7, 6, 8, 7, 8]},
    {"Surname": "Петренко", "Grades": [10, 9, 9, 10, 10]},
    {"Surname": "Мельник", "Grades": [6, 7, 6, 5, 7]},
    {"Surname": "Шевченко", "Grades": [8, 9, 7, 8, 9]},
    {"Surname": "Сидоренко", "Grades": [9, 8, 9, 9, 10]},
    {"Surname": "Олійник", "Grades": [7, 8, 7, 6, 8]},
    {"Surname": "Кравчук", "Grades": [10, 10, 9, 10, 9]},
    {"Surname": "Бондар", "Grades": [8, 8, 7, 9, 8]},
    {"Surname": "Гуменюк", "Grades": [6, 7, 6, 6, 7]}
]

# запис у файл JSON
with open("marks.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)

while True:
    print("\nОберіть дію:")
    print("1 - Переглянути дані")
    print("2 - Додати учня")
    print("3 - Порахувати середні оцінки")
    print("4 - Вийти")

    choice = input("Ваш вибір: ")

    if choice == "1":
        with open("marks.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            for s in data:
                print(s["Surname"], "-", s["Grades"])

    elif choice == "2":
        with open("marks.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        surname = input("Прізвище: ")
        grades = []
        for i in range(5):
            g = int(input(f"Оцінка з предмету {i+1}: "))
            grades.append(g)
        data.append({"Surname": surname, "Grades": grades})
        with open("marks.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("✅ Учня додано!")

    elif choice == "3":
        with open("marks.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        # середня оцінка кожного
        for s in data:
            s["Average"] = sum(s["Grades"]) / len(s["Grades"])
        # середня по класу
        class_avg = sum(s["Average"] for s in data) / len(data)
        print(f"\nСередня оцінка по класу: {class_avg:.2f}")
        print("Учні з середньою оцінкою вище за середню:")
        for s in data:
            if s["Average"] > class_avg:
                print(f"{s['Surname']} - {s['Average']:.2f}")

    elif choice == "4":
        print("👋 Вихід із програми.")
        break

    else:
        print("Невірний вибір, спробуйте ще раз.")




