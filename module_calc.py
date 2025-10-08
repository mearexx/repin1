
# module_calc.py

def series_sum(n):
    """
    Обчислює суму (1.1)^(2/1) + 3/2 + 4/3 + ... + (n+1)/n
    """
    result = 0
    for i in range(1, n + 1):
        result += (i + 1) / i
    result *= 1.1  # множимо перший елемент на 1.1
    return result
