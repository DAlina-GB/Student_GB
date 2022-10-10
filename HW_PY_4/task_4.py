# Задача №4
# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint

num = int(input('Задайте натуральную степень k: '))

coefficients = []
for i in range(num + 1):
    coefficients.append(randint(0,100)) 

polynomial = str() 
for i in range(num, -1, -1):
    if i == 0:
        polynomial += ('{}'.format(coefficients[i]))   
    elif i == 1:
        polynomial += ('{}x + ' .format(coefficients[i]))
    else:
        polynomial += ('{}x^{} + ' .format(coefficients[i], i))

print(polynomial)

data = open('task_4.txt', 'w')
data.writelines(polynomial)
data.close()