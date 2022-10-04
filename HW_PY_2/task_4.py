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