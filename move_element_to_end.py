"""
Move Element to End
You're given an array of integers and an integer. Write a function that moves all instances of that integer to the end
and returns the array.

The function should perform this in place (i.e., it should mutate the array in place) and doesn't need to maintain the
order of the other integers.
"""
from icecream import ic
from helpers import time_decorator
from helpers import random_range_integers as ra

# array = [2, 1, 2, 2, 2, 3, 4, 2]
array = [2, 1, 3, 2, 2, 5, 4, 2]
array_01 = ra(low=4, high=101, size=30, seed=2, unique=False)
to_move = 5

# k = {item: array_01.count(item) for item in set(array_01)}


def move_element_to_end_00(a, m):
    idx_01 = 0
    idx_02 = 1
    current = a[idx_01]
    current_1 = a[idx_01 + 1]
    mark = 0
    array_now = a

    while idx_01 + 1 < len(a):
        if a[idx_01] == m and a[idx_01 + 1] != m:
            idx_01 += 1
            a[mark], a[mark + 1] = a[mark + 1], a[mark]
            mark = idx_01
        elif a[idx_01] == m and a[idx_01 + 1] == m:
            idx_01 += 1
        # elif a[idx_01] != m and a[idx_01 + 1] != m:
        #     a[idx_01], a[idx_02] = a[idx_02], a[idx_01]
        # else:
        #     idx_01 += 1
        #     idx_02 += 1


@time_decorator
def move_element_to_end_01(a: list, m: int) -> list:
    moving = []
    staying = []
    for i in a:
        if i == m:
            moving.append(i)
        else:
            staying.append(i)
    return staying + moving


# # O(n) time | O(1) space - where n is the length of the array
@time_decorator
def move_element_to_end_ALGO(a: list, m: int) -> list:
    i = 0
    j = len(a) - 1
    while i < j:
        while i < j and a[j] == m:
            j -= 1
        if a[i] == m:
            a[i], a[j] = a[j], a[i]
        i += 1
    return a


@time_decorator
def move_element_to_end_02(a: list, m: int) -> list:
    l = 0
    r = len(a) - 1
    while l < r:
        while a[r] == m and l < r:
            r -= 1
        if a[l] == m:
            a[l], a[r] = a[r], a[l]
        l += 1
    return a


if __name__ == '__main__':
    a_01 = array_01
    t_01 = to_move
    # move_element_to_end_01(a_01, t_01)
    move_element_to_end_02(a_01, t_01)
    move_element_to_end_ALGO(a_01, t_01)
