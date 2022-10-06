# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def multiply_sp(sp):
    if len(sp) % 2 != 0:
        print("Количество элементов списка не четное!")
        rz = int(len(sp) / 2) + 1
    else:
        rz = int(len(sp) / 2)

    mult = []
    for i in range(0, rz):
        mult.append(sp[i] * sp[len(sp) - 1 - i])
    return mult


if __name__ == "__main__": 
     sp = [2, 3, 4, 5, 6]
print(sp, " => ", multiply_sp(sp))
