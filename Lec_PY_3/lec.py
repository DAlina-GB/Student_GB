# Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension

# def calc(x):
#     return x+10
# print(calc(10))
# def calc1(x):
#     return x*10
# print(calc1(10))

# def math(op, x):
#    print(op(x))

# math(calc1, 10)
#################################################################################

# составить список состоящий только из четых чисел
# list = []

# for i in range(1,101):
#     if(i%2 == 0):
#         list.append(i);
# print (list)


# list = [i for i in range (1,21)]                    # запись списка чисел
# print (list)                
# list = [i for i in range (1,21)if i%2 == 0]        # короткая запись списка из четных чисел
# print (list)
# list = [(i, i) for i in range (1,21)if i%2 == 0]        # короткая запись списка четных кортежей
# print (list)

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range (1,21)if i%2 == 0]        # кортежи четных чисел и возведение их в куб
# print (list)

# В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа).

# path ='/Users/alina/Desktop/Seminar PY/Lec_PY_3/file.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':                               #найти первую позицию пробела
#      space_pos = data.index(' ')
#      numbers.append(int(data[:space_pos]))
#      data = data[space_pos+1:]

# out = []
# for e in numbers:
#      if not e % 2:
#          out.append((e,e **2))
# print(out)

# укороченый вариант с использованием лямбд

# def select(f, col):
#      return [f(x) for x in col]
# def where(f, col):
#      return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split() 

# res = select(int, data)
# res = where(lambda x: not x % 2, res)  #проверка на четность
# res = select(lambda x: (x, x**2), res) 
# print (res)
 
