# Задача №5
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

dict = {}
keys = dict.keys()

def Degrees_and_Coefficients(polynomial, dictionary):
    for i in range(1, len(polynomial)):
        if polynomial[i] == '^':
            if int(polynomial[i + 1]) not in keys:
                dictionary[int(polynomial[i+1])] = 0
            digit = 1
            j = i-2
            while polynomial[j] != ' ' and j >= 0:
                dictionary[int(polynomial[i+1])] += (int(polynomial[j]) * digit)
                digit *= 10
                j = j-1
        elif polynomial[i] == 'x' and (polynomial[i + 1] == ' ' or i == len(polynomial) - 1):
            if 1 not in keys:
                dictionary[1] = 0
            digit = 1
            j = i-1
            while polynomial[j] != ' ' and j >= 0:
                dictionary[1] += (int(polynomial[j]) * digit)
                digit *= 10
                j = j-1
    k = len(polynomial)-1
    digit = 1
    while polynomial[k] != ' ':
        if i != 'x':
            if 0 not in keys:
                dictionary[0] = 0
            j = k
            if polynomial[j] == '^':
                dictionary[0] = 0
                break
            dictionary[0] += (int(polynomial[j]) * digit)
            digit *= 10
            j = j-1
            k -= 1
    return dictionary

path = '/Users/alina/Desktop/Seminar PY/HW_PY_4/res.txt'
data = open(path,'r')
for line in data:
    dict = Degrees_and_Coefficients(line, dict)
data.close()

path = '/Users/alina/Desktop/Seminar PY/HW_PY_4/res_2.txt'
data = open(path,'r')
for line in data:
    dict = Degrees_and_Coefficients(line, dict)
data.close()

polynomial = str() 
for i in range(max(keys), min(keys), -1):
    if i not in keys:
        continue
    polynomial += ('{}x^{} + ' .format(dict[i], i))
polynomial += ('{}'.format(dict[min(keys)]))

data = open('/Users/alina/Desktop/Seminar PY/HW_PY_4/task_5_result.txt', 'w')
data.writelines(polynomial)
data.close()

