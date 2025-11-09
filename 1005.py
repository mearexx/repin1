
# Програма для роботи зі словником students:
# - додавання / видалення записів,
# - перегляд відсортованих записів,
# - підрахунок середніх оцінок учнів і класу,
# - обробка типових помилок введення.

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

def average_grades(students_dict):
    """Повертає словник середніх оцінок для кожного учня.
       Якщо у студента немає оцінок — не додається в результат."""
    averages = {}
    for name, grades in students_dict.items():
        if not grades:
            # пропускаємо запис без оцінок
            continue
        try:
            avg = sum(grades) / len(grades)
        except Exception as e:
            print(f"Помилка при обчисленні для {name}: {e}")
            continue
        averages[name] = avg
    return averages

def class_average(averages_dict):
    """Повертає середню по класу (за словником середніх учнів).
       Якщо словник порожній — повертає None."""
    if not averages_dict:
        return None
    return sum(averages_dict.values()) / len(averages_dict)

def print_results(averages, class_avg):
    """Друкує середню по класу і прізвища учнів з середнім вище класового."""
    if class_avg is None:
        print("Немає даних для обчислення середнього по класу.")
        return
    print(f"\nСередня оцінка по класу: {class_avg:.2f}\n")
    print("Учні, у яких середня оцінка вище середньої по класу:")
    found = False
    for name, avg in averages.items():
        if avg > class_avg:
            print(f"{name}: {avg:.2f}")
            found = True
    if not found:
        print("Немає учнів із середнім вище за середнє по класу.")

def view_students_sorted(students_dict):
    """Виводить вміст словника, відсортований за ключами (іменами)."""
    if not students_dict:
        print("Словник пустий.")
        return
    print("\nСписок учнів (відсортовано за іменем):")
    for name in sorted(students_dict.keys()):
        grades = students_dict[name]
        print(f"{name}: {grades}")

def add_student(students_dict):
    """Додає нового учня в словник. Перевіряє коректність введення."""
    try:
        name = input("Введіть ключ-ім'я учня (наприклад Ivan_Petrenko): ").strip()
        if not name:
            print("Ім'я не може бути порожнім.")
            return
        if name in students_dict:
            print("Такий ключ вже існує. Якщо хочеш, видали старий запис або вибери інше ім'я.")
            return
        grades_input = input("Введіть оцінки через пробіл (кількість може бути будь-якою): ").strip()
        if not grades_input:
            print("Оцінки не введені — запис не створено.")
            return
        grades_strs = grades_input.split()
        grades = []
        for s in grades_strs:
            try:
                g = float(s) if ('.' in s or ',' in s) else int(s)
                # допускаємо як int, так і float; можна додатково перевіряти діапазон
                grades.append(g)
            except ValueError:
                print(f"Некоректна оцінка '{s}' — пропускаю цей елемент.")
        if not grades:
            print("Після обробки немає жодної коректної оцінки — запис не створено.")
            return
        students_dict[name] = grades
        print(f"Успішно додано учня {name}.")
    except Exception as e:
        print(f"Помилка при додаванні учня: {e}")

def remove_student(students_dict):
    """Видаляє учня за ключем з перевіркою існування."""
    try:
        name = input("Введіть ключ-ім'я учня для видалення: ").strip()
        if not name:
            print("Ім'я не може бути порожнім.")
            return
        if name not in students_dict:
            print("Ключ не знайдено.")
            return
        # підтвердження видалення
        confirm = input(f"Впевнені, що хочете видалити {name}? (y/n): ").strip().lower()
        if confirm == 'y':
            del students_dict[name]
            print(f"Учень {name} видалений.")
        else:
            print("Видалення скасовано.")
    except Exception as e:
        print(f"Помилка при видаленні учня: {e}")

def save_to_json(students_dict, filename="students.json"):
    """Опціонально: збереження словника у файл (JSON)."""
    import json
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(students_dict, f, ensure_ascii=False, indent=2)
        print(f"Дані збережено у {filename}.")
    except Exception as e:
        print(f"Помилка при збереженні у файл: {e}")

def load_from_json(filename="students.json"):
    """Опціонально: завантаження словника з JSON-файлу."""
    import json
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"Дані завантажено з {filename}.")
        return data
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено. Продовжую з поточними даними.")
        return None
    except Exception as e:
        print(f"Помилка при завантаженні файлу: {e}")
        return None

def main_menu():
    """Головне меню програми з обробкою помилок вводу."""
    global students
    while True:
        print("\nОберіть дію:")
        print("1 - Переглянути учнів (відсортовано)")
        print("2 - Додати учня")
        print("3 - Видалити учня")
        print("4 - Порахувати середні оцінки і вивести учнів вище середнього")
        print("5 - Зберегти у students.json")
        print("6 - Завантажити з students.json (перезапис поточних даних якщо успішно)")
        print("7 - Вийти")
        choice = input("Ваш вибір: ").strip()
        if choice == "1":
            view_students_sorted(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            remove_student(students)
        elif choice == "4":
            averages = average_grades(students)
            class_avg = class_average(averages)
            print_results(averages, class_avg)
        elif choice == "5":
            save_to_json(students)
        elif choice == "6":
            loaded = load_from_json()
            if loaded is not None:
                # Перевіряємо, що структура коректна (словник)
                if isinstance(loaded, dict):
                    students = loaded
                else:
                    print("Невірний формат файлу — очікувався словник.")
        elif choice == "7":
            print("Вихід. До побачення!")
            break
        else:
            print("Невірний вибір. Введіть число від 1 до 7.")

if __name__ == "__main__":
    main_menu()

