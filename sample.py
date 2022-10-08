import random
import time

def bubble_sort(number):
    len_number = len(number)
    for i in range(len_number):
        for j in range(len_number - 1 - i):
            if number[j] > number[j+1]:
                number[j], number[j+1] = number[j+1], number[j]
    return number


nums = [random.randint(0, 100) for _ in range(11)]
print(bubble_sort(nums))

a = 1
b = 2
