"""
Three Number Sum
Write a function that takes a non-empty array of distinct integers and an integer representing
a target sum. The function should find all triplets in the array that sum up to the target sum and return
a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending
order, and the triplets themselves likewise with respect to the numbers they hold.
If no three numbers sum up to the target sum, the function should return an empty array.
"""

from helpers import random_range_integers
from helpers import time_decorator

a_0 = [12, 3, 1, 2, -6, 5, -8, 6]
t_0 = 0

a_1 = [1, 2, 3]
t_1 = 6

a_2 = [5, -3, 1, 2, -6]
t_2 = 0

a_3 = [-2, 3, 0, 4, -9, 3]
t_3 = -1

a_4 = [-2, 3, 0, -4]
t_4 = 1


@time_decorator
def three_number_sum_00(array, target):
    long_list = []
    for i in range(len(array)):
        for i2 in range(i + 1, len(array)):
            for i3 in range(i2 + 1, len(array)):
                u = [array[i], array[i2], array[i3]]
                # print(u)
                s = array[i] + array[i2] + array[i3]
                l = sorted([array[i], array[i2], array[i3]])
                if s == target and l not in long_list:
                    long_list.append(l)
    return sorted(long_list)


@time_decorator
def three_number_sum_01(array, target):
    array.sort()
    long_list = []
    for i in range(len(array)):
        left = i + 1
        right = len(array) - 1
        for j in range(left, right):
            if left < right:
                current = array[i]
                left_ = array[left]
                right_ = array[right]
                s = current + left_ + right_
                l = [current, left_, right_]
                if s == target and l not in long_list:
                    long_list.append(l)
                    left += 1
                    right += 1
                elif s > target:
                    right -= 1
                elif s < target:
                    left += 1
        if array[i] > 0 and array[i] >= target:
            break
    return sorted(long_list)


if __name__ == '__main__':
    a = a_0
    t = t_0
    a = random_range_integers(-50, 60, 90)
    # three_number_sum_01(a, t)
    print(three_number_sum_00(a, t))
    print(three_number_sum_01(a, t))
