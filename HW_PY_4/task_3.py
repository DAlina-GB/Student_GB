# Задача №3
# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint

elements = []
count = 9
for i in range(count):
    elements.append(randint(0,9))
print(elements)   

unique_and_first_occurence = []
repeating_occurence = []
for i in elements:
    if i not in unique_and_first_occurence:
        unique_and_first_occurence.append(i)
    else:
        repeating_occurence.append(i)

result = []
for i in elements:
    if i not in repeating_occurence:
        result.append(i)
print(result)