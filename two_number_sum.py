from time import time
import numpy as np
from icecream import ic

"""
Write a function that takes a non-empty array of distinct integers and an integer
representing a target sum. If any two numbers in the input array sum up to the target sum,
the function should return them an an array, in any order. 
If no two numbers sum up th the target sum, the function should return an empty array.
Note that the target sum has to be obtained by summing two different integers in the array,
you can't add a single integer to itself in order to obtain the target sum.
You can assume that there will be at most one pair of numbers summing up to the target sum. 

"""

array_00 = [10, 15, 3, 7]
target_sum_00 = 17

array_01 = [3, 5, -4, 8, 11, 1, -1, 6, 7, 2, -14, 4]
target_sum_01 = 10

array_02 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
target_sum_02 = 18

np.random.seed(1)
arr = list(set(np.random.randint(low=-100, high=100, size=100)))

array_03 = arr
target_sum_03 = 18


def time_decorator(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


@time_decorator
def long_time(n):
    for i in range(n):
        for j in range(100000):
            i * j


@time_decorator
def two_number_sum_00(array, target_sum):
    seen = set()
    for num in array:
        if target_sum - num in seen:
            # ic(seen, num)
            return [target_sum - num, num]
        seen.add(num)
    return []


# O(n) time | O(n) space
@time_decorator
def two_number_sum_01(array, target_sum):
    nums = {}
    for num in array:
        potential_match = target_sum - num
        if potential_match in nums:
            ic(potential_match, num)
            return [potential_match, num]
        else:
            nums[num] = True
    return []


# O(n^2) time | O(1) space - mine
@time_decorator
def two_number_sum_02(array, target_sum):
    for idx, x in enumerate(array):
        for y in array[idx + 1:]:
            if x + y == target_sum:
                # ic(x, y)
                return [x, y]
    return []


# O(n^2) time | O(1) space
@time_decorator
def two_number_sum_03(array, target_sum):
    for i in range(len(array) - 1):
        first_num = array[i]
        for j in range(i + 1, len(array)):
            second_num = array[j]
            if first_num + second_num == target_sum:
                # ic(first_num, second_num)
                return [first_num, second_num]
    return []


# O(nlog(n)) | O(1) space
@time_decorator
def two_number_sum_04(array, target_sum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target_sum:
            # # ic(array[left], array[right])
            return [array[left], array[right]]
        elif current_sum < target_sum:
            left += 1
        elif current_sum > target_sum:
            right -= 1
    return []


if __name__ == "__main__":
    # two_number_sum_00(array_00, target_sum_00)
    array = array_01
    target_sum = target_sum_01
    ic(array, target_sum)
    # ic(two_number_sum_00(array, target_sum))
    # x = two_number_sum_01(array, target_sum)
    # ic(x)
    ic(two_number_sum_02(array, target_sum))
    # ic(two_number_sum_03(array, target_sum))
    # ic(two_number_sum_04(array, target_sum))
