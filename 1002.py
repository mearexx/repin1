def reverse_list():
    # Введення списку з клавіатури
    A = list(map(int, input("Enter a list: ").split()))
    print("Original list:", A)

    # Створення нового списку у зворотному порядку
    result = []
    for i in range(len(A) - 1, -1, -1):
        result.append(A[i])

    # Виведення результатів
    print("Reversed list:", result)
    print("Number of elements:", len(result))

    return result


reverse_list()

