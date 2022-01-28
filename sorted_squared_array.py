"""
Write a function that takes in a non-empty array of integers
that are sorted in ascending order and returns a new array
of the same length with the squares
of the original integers also sorted in an ascending order.
"""
from icecream import ic

array = [[1, 2, 3, 5, 6, 8, 9], [-5, -4, -3, -2, -1], [-10, -5, 0, 5, 10], [1, 4, 9, 25, 36, 64, 81], [1, 2]]


def sorted_squared_array(a):
    return sorted([x * x for x in a])


def sorted_squared_array_00(a):
    left = 0
    right = len(a) - 1
    out = []
    for i in a:
        if abs(a[left]) < abs(a[right]):
            out.append(abs(a[left]) ** 2)
            left += 1
        else:
            out.append(abs(a[right]) ** 2)
            right -= 1
    return out


def sorted_squared_array_01(a):
    left = 0
    right = len(a) - 1
    out = [1 for _ in a]
    for i in reversed(range(len(a))):
        if abs(a[left]) > abs(a[right]):
            out[i] = a[left] ** 2
            left += 1
        else:
            out[i] = a[right] ** 2
            right -= 1
    return out


# O(n) time | O(n) space - where n is the length of the input array
def sorted_squared_array_02(a):
    sorted_squares = [0 for _ in a]
    smaller_value_idx = 0
    larger_value_idx = len(a) - 1
    for idx in reversed(range(len(a))):
        smaller_value = a[smaller_value_idx]
        larger_value = a[larger_value_idx]
        if abs(smaller_value) > abs(larger_value):
            sorted_squares[idx] = smaller_value ** 2
            smaller_value_idx += 1
        else:
            sorted_squares[idx] = larger_value ** 2
            larger_value_idx -= 1
    return sorted_squares


if __name__ == '__main__':
    # [ic(sorted_squared_array_02(x)) for x in array]
    # [ic(sorted_squared_array_00(x)) for x in array]
    [ic(sorted_squared_array_01(x)) for x in array]
    # ic(sorted_squared_array_01(array[2]))
    # ic(sorted_squared_array_01(array[2]))
