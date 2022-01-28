"""
Smallest Difference
Write a function that takes in two non-empty arrays of integers,
finds the pair or numbers on from each array whose absolute difference is closest to zero,
and returns an array containing these two numbers,
with the number from the first array in the first position.
Note that the absolute difference between two integers is the
distance between them on the real number line.
For example, the absolute difference of -5 and 5 is 10,
and the absolute difference of -5 and -4 is 1.
You can assume that there will only be one pair of numbers with the smallest difference.

"""
from helpers import random_range_integers as ra
from icecream import ic

a_01 = [-1, 5, 10, 20, 28, 3]
a_02 = [26, 134, 135, 15, 17]
r = [28, 26]

a_11 = ra(-150, 150, 10)
a_12 = ra(-150, 150, 15)

a_21 = [-1, 5, 20, 3, 10]
a_22 = [26, 134, 135, 15, 17]

a_31 = [-1, 5, 10, 20, 28, 3]
a_32 = [26, 134, 135, 15, 17]

a_41 = [-1, 20, 3]
a_42 = [15, 17]

a_51 = [10, 0, 20, 25, 2000]
a_52 = [1005, 1006, 1014, 1032, 1031]

a_61 = [240, 124, 86, 111, 2, 84, 954, 27, 89]
a_62 = [1, 3, 954, 19, 8]

r = [28, 26]
d = {y: x for x, y in enumerate(a_01)}


def smallestDifference_02(arrayOne, arrayTwo):
    d_a = dict.fromkeys(arrayOne, 'a')
    d_b = dict.fromkeys(arrayTwo, 'b')

    shorter_d = {}
    if len(d_a) >= len(d_b):
        shorter_d = d_b
    else:
        shorter_d = d_a

    for d_b_k in shorter_d.keys():
        if d_b_k in d_a.keys():
            print([d_b_k, d_b_k])
            return [d_b_k, d_b_k]

    d_a.update(d_b)
    ds = {k: v for k, v in sorted(list(d_a.items()))}
    max_ = max(ds.keys())
    # c and n for current and next elements
    c, n = 0, 0

    for i in range(len(ds) - 1):
        key_c = int(list(ds.items())[i][0])
        key_n = int(list(ds.items())[i + 1][0])

        val_c = list(ds.items())[i][1]
        val_n = list(ds.items())[i + 1][1]

        diff = key_c - key_n
        # b, b = key_b, key_a
        if val_c != val_n:
            if diff < max_:
                max_ = diff
                c, n = key_c, key_n
                print('diff:', diff, 'key_c: ', key_c, 'key_n: ', key_n)
    print('RESULT: ', [c, n])
    return [c, n]


def smallestDifference_00(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    diff = max(max(arrayOne), max(arrayTwo))
    list_ = []
    for i in arrayOne:
        for j in arrayTwo:
            diff_tmp = abs(i - j)
            if diff_tmp < diff:
                diff = abs(i - j)
                list_.append([i, j])
    return list_[-1]  # diff


def smallestDifference_01(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    diff_dict = {}
    if len(arrayOne) >= len(arrayTwo):
        short_arr = arrayOne
        long_arr = arrayTwo
    else:
        long_arr = arrayOne
        short_arr = arrayTwo
    k = 0
    j = 0
    for i in range(len(long_arr) + len(short_arr)):
        j_ = short_arr[j + k]
        k_ = long_arr[k]
        j_1 = short_arr[j + k - 1]
        if k_ > short_arr[-1]:
            break
        if k_ < j_:
            diff_dict[k_ - j_1] = [k_, j_1]
            k += 1
            # j -= 1
        elif k_ > j_:
            j += 1
        # j += 1

    # return diff_dict[list(diff_dict.keys())[0]]
    return diff_dict


def smallestDifference_03(arrayOne, arrayTwo):
    d_a = dict.fromkeys(arrayOne, 'a')
    d_b = dict.fromkeys(arrayTwo, 'b')

    if len(d_a) >= len(d_b):
        shorter_d = d_b
        longer_d = d_a
    else:
        shorter_d = d_a
        longer_d = d_b

    for d_b_k in shorter_d.keys():
        if d_b_k in longer_d.keys():
            print([d_b_k, d_b_k])
            return [d_b_k, d_b_k]

    d_a.update(d_b)
    ds = {k: v for k, v in sorted(list(d_a.items()))}
    max_ = max(ds.keys())
    n, c = 0, 0  # n - next, c - current element

    for i in range(len(ds) - 1):
        key_c = int(list(ds.items())[i][0])
        key_n = int(list(ds.items())[i + 1][0])

        val_c = list(ds.items())[i][1]
        val_n = list(ds.items())[i + 1][1]

        diff = key_n - key_c
        if val_c != val_n:
            if diff < max_:
                max_ = diff
                n, c = key_n, key_c
                print('diff:', diff, 'key_n: ', key_n, 'key_c: ', key_c)

    if ds[c] == 'a':
        return [c, n]
    else:
        return [n, c]


# O(nlog(n) + mlog(m)) time | O(1) space
def smallestDiffFromAlgo(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float('inf')
    current = float('inf')
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair


if __name__ == '__main__':
    a = a_41
    b = a_42
    # ic(smallestDifference_00(a, b))
    # ic(smallestDifference_02(a, b))
    # ic(smallestDifference_03(a, b))
    ic(smallestDiffFromAlgo(a, b))
