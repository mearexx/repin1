def unique_letters():
    # Введення тексту
    A = input("Enter a text: ")

    # Переведення всіх символів у нижній регістр
    B = A.lower()

    print("Text:", B)

    # Множина унікальних символів
    S = set(B)

    # Формування множини літер, які зустрічаються лише один раз
    result = {ch for ch in S if B.count(ch) == 1}

    # Якщо множину неможливо сформувати напряму — перетворення через список
    if not result:
        temp_list = [ch for ch in B if B.count(ch) == 1]
        result = set(temp_list)

    print("Letters that appear once:", result)

    return result


# Виклик функції
unique_letters()


