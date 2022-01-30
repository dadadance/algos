"""
Longest Peak
Write a function that takes in na array of integers and returns the length of the longest peak in the
array. A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the
highest values in the peak), at which point they become strictly decreasing. At least three integers are required to
form a peak. For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do the
integers 1, 2, 2, 0. Similarly, the integers 1, 2, 3 do not form a peak because there aren't any strictly decreasing
integers after the 3.
Sample input:   "array": [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
Sample output: 6 // 0, 10,
6, 5, -1, -2
"""

a_01 = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
a_02 = []
a_03 = [1, 3, 2]
a_04 = [1, 2, 3, 4, 5, 1]
a_05 = [5, 4, 3, 2, 1, 2, 1]
a_06 = [5, 4, 3, 2, 1, 2, 10, 12, -3, 5, 6, 7, 10]
a_07 = [5, 4, 3, 2, 1, 2, 10, 12]
a_08 = [1, 2, 3, 4, 5, 6, 10, 100, 1000]
a_09 = [1, 2, 3, 3, 2, 1]
a_10 = [1, 1, 3, 2, 1]
a_11 = [1, 2, 3, 2, 1, 1]
a_12 = [1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1]
a_13 = [1, 2, 3, 3, 4, 0, 10]


def longest_peak(array):
    one = 0
    two = 1
    three = 2

    peak = 0

    while one <= len(array) - 3:
        print(array[one], array[two], array[three])

        

        one += 1
        two += 1
        three += 1


if __name__ == '__main__':
    # b = a_08
    b = a_01
    longest_peak(b)
