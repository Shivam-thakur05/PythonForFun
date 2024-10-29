'''
You are given a list of integers. Write a Python function that performs the following operations:

Iterate through the list and create a new list that contains only the even numbers from the original list.
For each even number in the new list, replace it with the square of that number if it is greater than 10. Otherwise, leave it unchanged.
'''

import numpy as np

# Original list of numbers
nums = [4, 11, 8, 15, 12, 7, 10]

# Create a NumPy array from the list
nums_array = np.array(nums)

# Filter even numbers
even_nums = nums_array[nums_array % 2 == 0]

# Replace numbers greater than 10 with their square
result = [x**2 if x > 10 else x for x in even_nums]

print(result)



