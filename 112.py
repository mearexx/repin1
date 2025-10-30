sentence = input("Введіть речення: ")

# Розділяємо речення на слова
words = sentence.split()

# Перетворюємо список слів у множину, щоб прибрати повтори
unique_words = set(words)

print("Різні слова у реченні:")
for word in unique_words:
    print(word)
