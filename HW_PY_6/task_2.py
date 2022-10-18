# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

num = int(input('Введите число k: '))
elements = [(1 + 1/(x + 1)) ** (x + 1) for x in range(num)]
print(elements)
result = sum(elements)
print(result)
