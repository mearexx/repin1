import requests
from lxml import html
import csv
import sys

# 1. Функція отримання HTML із сайту

def fetch_html(url: str) -> str:
    try:
        print("Завантаження даних з сайту...")
        response = requests.get(url, timeout=10)

        response.raise_for_status()   # помилки 4xx, 5xx
        return response.text

    except requests.exceptions.RequestException as e:
        print("Помилка HTTP:", e)
        raise

# 2. Функція парсингу HTML та витягу новин


def parse_news(html_text: str) -> list:
    
    print("Парсинг HTML...")

    try:
        doc = html.fromstring(html_text)

        # Новий актуальний XPath для Hacker News
        titles = doc.xpath('//span[@class="titleline"]/a/text()')
        links  = doc.xpath('//span[@class="titleline"]/a/@href')

        news_list = []

        for title, link in zip(titles, links):
            news_list.append({
                "title": title.strip(),
                "link": link.strip(),
                "length": len(title.strip())
            })

        return news_list

    except Exception as e:
        print("Помилка парсингу:", e)
        raise

# 3. Простий аналіз даних

def analyze_news(news: list) -> dict:

    print(" Аналіз даних...")

    lengths = [item["length"] for item in news]

    return {
        "count": len(lengths),
        "min_length": min(lengths),
        "max_length": max(lengths),
        "avg_length": sum(lengths) / len(lengths)
    }

# 4. Збереження результатів у CSV

def save_to_csv(news: list, filename="news.csv"):

    print("Збереження CSV")

    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["title", "link", "length"])
            writer.writeheader()
            writer.writerows(news)
    except Exception as e:
        print("Помилка запису CSV:", e)
        raise

# 5. Збереження аналізу у TXT

def save_analysis(results: dict, filename="analysis.txt"):

    print("Збереження TXT...")

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Результати аналізу заголовків новин:\n")
            file.write(f"Кількість новин: {results['count']}\n")
            file.write(f"Мінімальна довжина: {results['min_length']}\n")
            file.write(f"Максимальна довжина: {results['max_length']}\n")
            file.write(f"Середня довжина: {results['avg_length']:.2f}\n")
    except Exception as e:
        print("Помилка запису TXT:", e)
        raise


# 6. Головна функція

def main():
    print("============== ПРОГРАМА ВЕБ-СКРЕЙПІНГУ ==============")
    
    url = input("Введіть URL сайту (або натисніть Enter для стандартного): ")

    if not url.strip():
        url = "https://news.ycombinator.com/"

    try:
        html_text = fetch_html(url)
        news = parse_news(html_text)

        if not news:
            print("Не знайдено жодної новини")
            sys.exit()

        analysis = analyze_news(news)

        save_to_csv(news)
        save_analysis(analysis)

        print("\nГотово. Результати збережено у файли:")
        print(" news.csv")
        print("analysis.txt")

        print("\nКороткий аналіз:")
        print(f"Новин знайдено: {analysis['count']}")
        print(f"Середня довжина заголовка: {analysis['avg_length']:.2f}")

    except Exception:
        print("Програма завершена через помилку.")

main()
