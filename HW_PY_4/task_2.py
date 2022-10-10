# Задача №2
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Какое-то неправильное число!")
    return number


def func_search(num):
    rezult = []

    for i in range(2, num):
        while num % i == 0:
            num /= i
            rezult.append(i)
    return rezult


num = InputNumbers("Введите натуральное число N: ")


print(f"Результат деления: {func_search(num)}")


