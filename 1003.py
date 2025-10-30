def every_second_element():
    # Введення списку з клавіатури
    A = list(map(int, input('Enter a list of numbers: ').split()))
    
    print('Original list:', A)
    
    # Формування нового списку — кожен другий елемент
    new_list = A[1::2]
    
    print('New list (every second element):', new_list)
    
    return new_list

# Виклик функції
every_second_element()

