# Реализуйте алгоритм перемешивания списка.
from random import randint
import math 

nums = [1111, 23, 348889, 4, 55, 67777777, 0.8, -0.8]
print(nums)

for i in range(len(nums)):
    temp = nums[i]
    new_index = randint(0, len(nums)-1)
    nums[i] = nums[new_index]
    nums[new_index] = temp

print(nums)

# Решение с семинара

# Реализуйте алгоритм перемешивания списка.
# n = int(input("Введите количество элементов: "))
# input_list = [i for i in range(n)]
# result_list = input_list[:]
# for i in range(n):
# index_random = random.randint(0, n - 1)
# result_list[i], result_list[index_random] = result_list[index_random], result_list[i]
# # temp = result_list[i]
# # result_list[i] = result_list[index_random]
# # result_list[index_random] = temp
# print("Исходный список",input_list)
# print("Перемешанный список",result_list)
