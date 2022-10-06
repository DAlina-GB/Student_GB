# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
#  [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#  [Негафибоначчи]

def fibo(n):
    fibo_list = list()
    fibo_list.append(0)
    fibo_list.append(1)

    for i in range(2, n + 1):
        fibo_list.append(fibo_list[i - 1] + fibo_list[i - 2])

    fibo_list.insert(0, 1)
    fibo_list.insert(0, -1)

    for i in range(0, n - 2):
        fibo_list.insert(0, (fibo_list[1]) - (fibo_list[0]))
    return fibo_list


x = fibo(8)
print(x)


# Решения с семинара
# Вариант 1
# def nega_fibonacci(n):
# list_negafibonacci = [0]
# if n == 0:
# return list_negafibonacci
# elif n == 1:
# list_negafibonacci = [1, 0, 1]
# return list_negafibonacci
# else:
# list_negafibonacci = [-1, 1, 0, 1, 1]
# fib1 = fib2 = 1
# for i in range(2, n):
# fib1, fib2 = fib2, fib1 + fib2 # fib1 приравнивается к fib2, fib2 приравнивается к fib1 + fib2
# list_negafibonacci.append(fib2)
# list_negafibonacci.insert(0, (fib2 * (-1) ** i))
# return list_negafibonacci


# n = int(input("Введите число: "))
# print((f"Список чисел (нега)Фибоначчи для k = {n}: {nega_fibonacci(n)}"))

