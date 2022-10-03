# import random
# import copy


# my_list = [[1,2], [3,4]] #вложеный список
# # my_list2 = my_list[:]       - не правильно
# my_list2 = copy.deepcopy(my_list) # правильно
# my_list[0].append(5)
# print (my_list2)


# Найдите произведение элементов на указаннных позициях.
# Позиции храняться в файле file.txt в одной строке одно число.

positions = []
with open('file.txt', 'r', encoding='utf-8') as f:
    positions = f.read().split()
positions = [int(i) for i in positions]
n = int(input('Введите целое число: '))
s = []
for i in range(-n, n + 1):
    s.append(i)
result = 1
for i in range(len(positions)):
    result *= s[positions[i] - 1]
print(f'Исходный список: {s}.\nПозиции: {positions}.')
print(result)