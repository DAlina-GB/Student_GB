# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

from random import randint


items = [randint(0,9) for x in range(5)]
print(items)
def element_for_index(num):
    global items
    return items[num]
elements_to_find = list(map(element_for_index, filter(lambda x: x%2, range(len(items)))))
result = sum(elements_to_find)
print(result)