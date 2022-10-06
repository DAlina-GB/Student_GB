# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

a = [1.1, 1.2, 3.1, 5.10, 10.01]


def average(n):
    max = 0
    min = 1
    for i in n:
        temp = round(i % 1, 3)
        if temp > max:
            max = temp
        elif temp < min:
            min = temp
    print(f"max {max} min {min}")
    res = max - min
    print("Разница между min и max", res)


average(a)

# Решение с семинара:
# input_list = input("Введите список чисел, разделенных пробелом: ").split()
# fract_list = []
# i_max = 0
# i_min = 0
# for i in range(len(input_list)):
# if float(input_list[i]) % 1 != 0:
# j = round((float(input_list[i]) % 1), 2)
# fract_list.append(j)
# for i in range(len(fract_list)):
# if fract_list[i] > fract_list[i_max]:
# i_max = i
# if fract_list[i] < fract_list[i_min]:
# i_min = i
# res = float(fract_list[i_max]) - float(fract_list[i_min])
# print("Список исходный значений: ", input_list)
# #print("Список дробных частей исходный значений:\n",fract_list)
# print("Разница между максимальным и минимальным значением дробной части элементов: ", res)
