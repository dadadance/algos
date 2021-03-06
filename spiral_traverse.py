"""
Spiral Traverse

Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n==m)
and returns a one-dimensional array of all the array's elements in spiral order.

Spiral order starts at the top left corner of the two-dimensional array,
goes to the rights, and proceeds in a spiral pattern all the way
until every element has been visited.
"""
from icecream import ic

a_00 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a_01 = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]

a_02 = [[1]]

a_03 = [
    [1, 2],
    [4, 3]
]

a_04 = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]

a_05 = [[1, 2, 3, 4, 5, 6],
        [20, 21, 22, 23, 24, 7],
        [19, 32, 33, 34, 25, 8],
        [18, 31, 36, 35, 26, 9],
        [17, 30, 29, 28, 27, 10],
        [16, 15, 14, 13, 12, 11]]

a_005 = [[1, 2, 3, 4, 5],
         [18, 19, 20, 21, 6],
         [17, 28, 29, 22, 7],
         [16, 27, 30, 23, 8],
         [15, 26, 25, 24, 9],
         [14, 13, 12, 11, 10]]

a_06 = [
    [19, 32, 33, 34, 25, 8],
    [16, 15, 14, 13, 12, 11],
    [18, 31, 36, 35, 26, 9],
    [1, 2, 3, 4, 5, 6],
    [20, 21, 22, 23, 24, 7],
    [17, 30, 29, 28, 27, 10]
]

a_006 = [
    [4, 2, 3, 6, 7, 8, 1, 9, 5, 10],
    [12, 19, 15, 16, 20, 18, 13, 17, 11, 14]
]

a_007 = [
    [27, 12, 35, 26],
    [25, 21, 94, 11],
    [19, 96, 43, 56],
    [55, 36, 10, 18],
    [96, 83, 31, 94],
    [93, 11, 90, 16]
]

a_008 = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
]

a_012 = [
    [1],
    [3],
    [2],
    [5],
    [4],
    [7],
    [6]
]


# #  EXAMPLE
# [a_05[0][i] for i in range(0, 6)]  # Horizontal
# [a_05[i][5] for i in range(1, 6)]  # Vertical
#
# [a_05[5][i] for i in reversed(range(0, 5))]
# [a_05[i][0] for i in reversed(range(1, 5))]
#
# [a_05[1][i] for i in range(1, 5)]
# [a_05[i][4] for i in range(2, 5)]
#
# [a_05[4][i] for i in reversed(range(1, 4))]
# [a_05[i][1] for i in reversed(range(2, 4))]
#
# [a_05[2][i] for i in range(2, 4)]
# [a_05[i][3] for i in range(3, 4)]
#
# [a_05[3][i] for i in reversed(range(2, 3))]
# [a_05[i][2] for i in reversed(range(3, 3))]  # end
#
# # EXAMPLE 2
# [a_005[0][i] for i in range(0, 5)]  # Horizontal left->right
# [a_005[i][4] for i in range(1, 6)]  # Vertical down
#
# [a_005[5][i] for i in reversed(range(0, 4))]  # Horizontal right->left
# [a_005[i][0] for i in reversed(range(1, 5))]  # Vertical up
#
# [a_005[1][i] for i in range(1, 4)]
# [a_005[i][3] for i in range(2, 5)]
#
# [a_005[4][i] for i in reversed(range(1, 4))]
# [a_005[i][1] for i in reversed(range(2, 4))]
#
# [a_005[2][i] for i in range(2, 3)]
# [a_005[i][2] for i in range(3, 4)]
#
# [a_005[3][i] for i in reversed(range(2, 3))]
# [a_005[i][2] for i in reversed(range(3, 3))]  # end

# # EXAMPLE 2 make a function
# b = a_005
# b = a_006
# b = a_012
# b = a_05
b = a_03
width = len(b[0])
height = len(b)
first = 0
second = width - 1
start = 0

while width - start > 0:
    print([b[first][i] for i in range(start, width)])  # Horizontal left->right
    print([b[i][width - 1] for i in range(start + 1, height)])  # Vertical down

    if len([b[height - 1][i] for i in reversed(range(start, width - 1))]) <= 0:
        break
    print([b[height - 1][i] for i in reversed(range(start, width - 1))])  # Horizontal right->left

    print([b[i][first] for i in reversed(range(start + 1, height - 1))])  # Vertical up
    first += 1
    start += 1
    width -= 1
    height -= 1


def do_the_spiral(array):
    print(type(array[0]))
    if not isinstance(array[0], list):
        return array
    elif len(array[0]) == 1:
        return [val for sublist in array for val in sublist]

    result = []
    width = len(array[0])
    height = len(array)
    start = 0
    while width - 1 or height - 1 > 0:
        one = [array[start][i] for i in range(start, width)]
        if len(one) > 0:
            print(one)
            result.extend(one)
        else:
            break

        two = [array[i][width - 1] for i in range(start + 1, height)]
        if len(two) > 0:
            print(two)  # Vertical down
            result.extend(two)
        else:
            break

        three = [array[height - 1][i] for i in reversed(range(start, width - 1))]
        if len(three) > 0:
            print(three)  # Horizontal right->left
            result.extend(three)
        else:
            break

        four = [array[i][start] for i in reversed(range(start + 1, height - 1))]
        if len(four) > 0:
            print(four)  # Vertical up
            result.extend(four)
        else:
            break

        start += 1
        width -= 1
        height -= 1
    return result

if __name__ == '__main__':
    # a = a_007
    a = a_008
    # spiral_traverse_01(a_01)
    print(do_the_spiral(a))
    # ic(func(a))
