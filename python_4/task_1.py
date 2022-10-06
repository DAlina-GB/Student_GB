# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел. 
 
# lst = list(map(float, input("Введите числа через пробел:\n").split()))
# new_lst = [round(i%1,2) for i in lst if i%1 != 0]
# print(max(new_lst) - min(new_lst))

# input_list = list(map(int, input("Введите числа через пробел:\n").split()))
# print(max(input_list),min(input_list))

#Вариант 2
nums = list(map(int, input('Введите числа через пробел: ').split()))

nums = input('Введите числа через пробел: ').split()
l_ist = [int(nums[i]) for i in range(len(nums))]
l_ist = [int(i) for i in nums]
print(l_ist)
nums = [int(i) for i in input('Введите числа через пробел: ').split()] # list comprehension
print(nums)
print(max(nums), min(nums)) 
print(max(nums), min(nums), sep= '+') 
print(str(max(nums)) + ' ' + str(min(nums)))
print(f'{max(nums)} {min(nums)}')