import os

os.system("cls" if os.name == "nt" else "clear")


# colors = ["red", "green", "blue"]
# with open("file.txt", "a") as data:
#     # data = open("file.txt", "a")
#     # data.writelines(colors)
#     data.write("Line_2\n")
#     data.write("Line_3\n")
# data.close()
# path1 = "file.txt"
# data = open("file.txt", "r")
# for l2 in data:
#     print(l2)
# data.close()

# import prog as p

# num = p.InputNumbers("Введите число: ")
# p.checkNumber(num)

# print(prog.f(1))
# def new_string(symbol, count=3):
#     return symbol * count


# print(new_string("!", 8))


# def func(*param):
#     rez: str = ""
#     for i in param:
#         rez += i
#     return rez


# print(func("1", "wqer", "845.25", "ss3"))


# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)


# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)


# Кортежи
# a = (5, 6)
# print(a[0])


# colors = ["red", "green", "blue"]
# print(colors)
# t = tuple(colors)
# print(t)

# словари

# dictionary = {"up": "↑", "left": "←", "down": "↓", "right": "→"}

# for k in dictionary.keys():
#     print(k)

# for v in dictionary.values():
#     print(v)
# del dictionary["left"]

# for x in dictionary:
#     print(dictionary[x])


# множества
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}

c = a.copy()  # c = {1, 2, 3, 5, 8}
u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)  # i = {8, 2, 5}
dl = a.difference(b)  # dl = {1, 3}
dr = b.difference(a)  # dr = {13, 21}
q = a.union(b).difference(a.intersection(b))
# {1, 21, 3, 13}
b = frozenset(a)

asd = [1, 2, 3, 5, 8]

print(asd.pop(2))
print(asd)
# print(asd.insert(2, 11))
asd.insert(2, 11)
print(asd)
asd.append(458)
print(asd)

