# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

task = str()

path = '/Users/alina/Desktop/Seminar PY/HW_PY_5/data_task4.txt'
data = open(path, 'r')
for line in data:
    task = line
data.close()


result = str()
count = 1

if len(task) == 1:
    result += task[0] + str(len(task))
elif len(task) != 0:
    temp = task[0]
    for i in range(1, len(task)):
        if task[i] == temp:
            count +=1
        else:
            result += task[i-1] + str(count)
            temp = task[i]
            count = 1
    result += task[i] + str(count)

with open('/Users/alina/Desktop/Seminar PY/HW_PY_5/result_task4.txt', 'w') as data:
    data.write(result)

# Модуль восстановления
task = str()

path = '/Users/alina/Desktop/Seminar PY/HW_PY_5/result_task4.txt'
data = open(path, 'r')
for line in data:
    task = line
data.close()

task += ' '
item = str()
num = str()
result = str()

for i in task:
    if not i.isdigit():
        if len(num) != 0 or i == ' ':
            result += int(num) * item
            item = i
            num = str()
        else: item = i
    else:
        num += i

with open('/Users/alina/Desktop/Seminar PY/HW_PY_5/recovery_task4.txt', 'w') as data:
    data.write(result)
