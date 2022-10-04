# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44, 5: 2.49, 6: 2.52}

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть целое ")
    return number

num = InputNumbers("Введите число n: ")
elements = []
for i in range(num):
    elements.append((1 + 1/(i + 1)) ** (i + 1))

print(elements)

sum1 = 0
for i in range(num):
    sum1 += elements[i]

print(sum1)

