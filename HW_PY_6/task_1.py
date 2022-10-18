# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def find_elements(x):
    if x == 1:
        return 1
    else: return x * find_elements(x - 1)

num = int(input('Введите число N: '))
items = [find_elements(x) for x in range(1, num + 1)]
print(items)
