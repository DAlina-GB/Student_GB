# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(n):
    if n in [1, 2]:
        return 1
    elif n < 1:
        return fibonacci(n + 2) - fibonacci(n + 1)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input('Введите число: '))
items = [x for x in range(-num, num + 1)]
result = list(map(fibonacci, items))
print(result)
