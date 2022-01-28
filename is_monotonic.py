"""
Monotonic Array
Write a function that takes in an array of integers and returns a boolean
representing whether the array is monotonic or not not.

An array is said to be monotonic if its elements, from left to right,
are entirely non-increasing or entirely non-decreasing.

Non-increasing element aren't necessarily exclusively decreasing, they simply do not increase.
Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.

Note that empty arrays and arrays of one element are monotonic.

"""

from icecream import ic

a = [[-1, -5, -10, -1100, -1100, -1101, -1102, -9001], [], [1], [1, 2], [2, 1], [1, 5, 10, 1100, 1101, 1102, 9001],
     [-1, -5, -10, -1100, -1101, -1102, -9001], [-1, -5, -10, -1100, -900, -1101, -1102, -9001], [1, 2, 0],
     [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11], [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11],
     [-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -7, -9, -10, -11],
     [-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11], [-1, -1, -1, -1, -1, -1, -1, -1],
     [1, 2, -1, -2, -5], [-1, -5, 10], [2, 2, 2, 1, 4, 5], [1, 1, 1, 2, 3, 4, 1], [1, 2, 3, 3, 2, 1]]

d = {0: [-1, -5, -10, -1100, -1100, -1101, -1102, -9001],
     1: [],
     2: [1],
     3: [1, 2],
     4: [2, 1],
     5: [1, 5, 10, 1100, 1101, 1102, 9001],
     6: [-1, -5, -10, -1100, -1101, -1102, -9001],
     7: [-1, -5, -10, -1100, -900, -1101, -1102, -9001],
     8: [1, 2, 0],
     9: [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11],
     10: [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11],
     11: [-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -7, -9, -10, -11],
     12: [-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11],
     13: [-1, -1, -1, -1, -1, -1, -1, -1],
     14: [1, 2, -1, -2, -5],
     15: [-1, -5, 10],
     16: [2, 2, 2, 1, 4, 5],
     17: [1, 1, 1, 2, 3, 4, 1],
     18: [1, 2, 3, 3, 2, 1]}


def is_monotonic_00(array):
    increasing = False
    decreasing = False
    i = 0
    while i < len(array) - 1:
        if array[i] < array[i + 1]:
            increasing = True
            decreasing = False
        elif array[i] > array[i + 1]:
            decreasing = True
            increasing = False
        i += 1
    return increasing, decreasing


def is_monotonic_01(array):
    i = 0
    diff = 0
    monotonic = True
    while i < len(array) - 1 and len(array) > 3:
        now_diff = abs(array[i + 1] - array[i])
        if now_diff > diff:
            diff = now_diff
            monotonic = True
        else:
            return False
        i += 1
    return monotonic


def is_monotonic_03(array):
    i = 0
    diff = 0
    while i < len(array) - 1 and len(array) > 2:
        if abs(array[i + 1] - array[i]) >= diff:
            diff = abs(array[i + 1] - array[i])
        else:
            return False
        i += 1
    return True


def is_monotonic_02(array):
    i = 0
    diff = 0
    m = True
    while i < len(array) - 1 and len(array) > 2:
        # print(array[i+1] - array[i])
        print(array[i] >= array[i + 1])
        if (array[i] >= array[i + 1]) != m_now:
            return False
        m_now = (array[i] >= array[i + 1])
        i += 1
    return True


def is_monotonic_03(array):
    i = 0
    r = []
    while i < len(array) - 1 and len(array) > 2:
        r.append((array[i] >= array[i + 1]))
        print((array[i] >= array[i + 1]))
        i += 1
    if len(set(r)) > 1:
        m = False
    else:
        m = True
    return m


def is_monotonic_04(array):
    i = 0
    r = []
    # first = array[0] - array[1] >= 0
    while i < len(array) - 1 and len(array) > 2:
        r.append(array[i + 1] - array[i] >= 0)
        print(array[i + 1] - array[i] >= 0)
        i += 1
    if len(set(r)) > 1:
        m = False
    else:
        m = True
    return m


def is_monotonic_05(array):
    i = 1
    if array[1] - array[0] >= 0 or array[1] - array[0] == 0:
        first = 1
    else:
        first = 0
        # first = array[1] - array[0] >= 0
    while i < len(array) - 1 and len(array) > 2:
        if array[i + 1] - array[i] >= 0 or array[i + 1] - array[i] == 0:
            m = 1
        else:
            m = 0
        print(array[i], array[i + 1])
        if m != first:
            return False
        first = m
        i += 1
    return True


def is_monotonic_06(array):
    i = 0
    decreasing = False
    decreasing_int = 1
    increasing = False
    increasing_int = 1
    final = False
    while i < len(array) - 1 and len(array) > 2:
        if array[i] >= array[i + 1]:
            decreasing = True
        else:
            decreasing_int = 0
        if array[i] <= array[i + 1]:
            increasing = True
        else:
            increasing_int = 0
        # ie, if either changed, then it means not monotonic
        if (decreasing_int == 0 and increasing == False) \
                or (increasing_int == 0 and decreasing == False) \
                or (decreasing == True and increasing == True):
            return False
        i += 1
    if decreasing:
        final = decreasing
    else:
        final = increasing
    return final


def is_monotonic_07(array):
    i = 0
    decreasing = False
    increasing = False
    while i < len(array) - 1 and len(array) > 2:
        if array[i] > array[i + 1] or array[i + 1] - array[i] < 0:
            decreasing = True
        elif array[i] < array[i + 1] or array[i + 1] - array[i] > 0:
            increasing = True
        if decreasing == True and increasing == True:
            return False
        i += 1
    f = max(decreasing, increasing)
    if len(array) < 3 or sum(array) / len(array) == array[0]:
        f = True
    return f


def is_monotonic_ALGO(array):
    is_non_increasing = True
    is_non_decreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i + 1]:
            is_non_decreasing = False
        if array[i] > array[i + 1]:
            is_non_increasing = False
    return is_non_increasing or is_non_decreasing


if __name__ == '__main__':
    # x = a[0]
    # x = d[5]
    # x = d[1]
    # x = d[2]
    # x = a[3]
    # x = a[10]
    # x = a[14]
    x = a[10]

    ic(x)
    # ic(is_monotonic_05(x))
    # ic(is_monotonic_04(x))
    # ic(is_monotonic_06(x))
    ic(is_monotonic_07(x))
