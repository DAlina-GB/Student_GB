# Напишите программу, которая принимает на вход число N и выдает 
# набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть целое ")
    return number


def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


num = InputNumbers("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")

# Решения с семинара
# n = int(input("Введите целое число N: "))
# m = 1
# res_list = []
# for i in range(1, n + 1):
# m *= i 
# res_list.append(int(m))
# print(f"Набор произведений чисел от 1 до {n}:", res_list)