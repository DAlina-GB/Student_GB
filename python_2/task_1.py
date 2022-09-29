# Напишите программу, которая принимает на вход число N и выдаёт 
# последовательность из N членов. (умножаем на -3)
# Пример:
# Для N = 5: 1, -3, 9, -27, 81

# n = int (input ("Input number N "))
# j = 1
# for i in range ( 1, n + 1):
#     print (j, end = ", ")
#     j =j * -3

# более красивое решение   
n = int(input("Введите чило N: "))
j = 1
list1 = []
for i in range(1, n + 1):
    list1.append(str(j))
    j = j * -3
print(", ".join(list1))
