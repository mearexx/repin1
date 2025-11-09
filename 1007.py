import csv
import os

flag = False

# --- спроба відкрити основний файл ---
try:
    csvfile = open("Exports.csv", "r", encoding="utf-8")
    reader = csv.DictReader(csvfile, delimiter=";")

    print("Country Name | 2018 [YR2018] | 2019 [YR2019]")
    for row in reader:
        print(row["Country Name"], ":", row["2018 [YR2018]"], "|", row["2019 [YR2019]"])

    csvfile.close()

except:
    print("Файл Exports.csv не знайдено!")


# --- пошук даних за введеними назвами країн ---
try:
    csvfile = open("Exports.csv", "r", encoding="utf-8")
    reader = csv.DictReader(csvfile, delimiter=";")

    print("\nВведіть назви країн через кому (наприклад: Ukraine, Italy, France): ")
    countries = input().split(",")

    countries = [c.strip().capitalize() for c in countries]  # очищення пробілів

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Результати пошуку:")

    with open("Exports_search_results.csv", "w", newline="", encoding="utf-8") as csvfile2:
        writer = csv.writer(csvfile2, delimiter=";")
        writer.writerow(["Country Name", "2018 [YR2018]", "2019 [YR2019]"])

        for row in reader:
            if row["Country Name"].capitalize() in countries:
                flag = True
                print(row["Country Name"], ":", row["2018 [YR2018]"], "|", row["2019 [YR2019]"])
                writer.writerow((row["Country Name"], row["2018 [YR2018]"], row["2019 [YR2019]"]))

    csvfile.close()

    if not flag:
        print("Жодна з введених країн не знайдена у файлі.")

except:
    print("Файл Exports.csv не знайдено!")

