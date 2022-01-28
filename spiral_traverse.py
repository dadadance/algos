"""
Spiral Traverse

Write a funciton that takes in an n x m two-dimensional array (that can be square-shaped when n==m)
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

a_005 = [[1, 2, 3, 4,     5],
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


def spiral_traverse(arr):
    horizontal_direction, horizontal_count = True, 0
    vertical_direction, vertical_count = True, 0
    result = []
    i, j = 0, 0
    while i < len(arr):
        j = 0
        while j < len(arr[i]):
            print(arr[i][j])
            j += 1
        i += 1
        horizontal_direction = -1


#
#
# x, y = 0, 0
# rng_v, rng_h = len(a_01), len(a_01)
# i = 0
# while i < len(a_01) ** 2:
#     if y == rng_v:
#         rng_v -= 1
#     if x == rng_h:
#         rng_h -= 1
#
#     if x == rng_v and y == rng_h:
#         rng_v -= 1
#         rng_h -= 1
#         direction = -1
#         y += 1
#         print(a_01[x][y])
#     print(a_01[x][y])
#     x += 1  # 0123

# for i in a_01:
#     print(i)
#
# for i in a_01[1]:
#     print(i)
#
# for i in range(0, len(a_01)):
#     print(a_01[0][i])
#
# for i in range(1, len(a_01)):
#     print(a_01[i][-1])
#
# for i in range(0, len(a_01))[::-1]:
#     print(a_01[3][i])
#
# for i in range(1, len(a_00))[-1]:
#     print(i)

# [a_01[0][i] for i in range(0, 4)]
# [a_01[i][3] for i in range(1, 4)]
#
# [a_01[3][i] for i in reversed(range(0, 3))]
# [a_01[i][0] for i in reversed(range(1, 3))]
#
# [a_01[1][i] for i in range(1, 3)]
# [a_01[i][2] for i in range(2, 3)]


start = 0
end = len(a_007)
width = len(a_007[0])
height = len(a_007)
first = 0
second = len(a_007) - 1

result = []
k = 0
i = 0
row, col = 0, 0
rng = width
while k < height:
    while i < rng:
        print(a_007[row][i])
        i += 1
    height -= 1
    row += 1
    rng = height
    i = 0
    k += 1
minus = -1
first = 3
second = 5

while second > 0:
    print(a_007[first][second])
    y += minus
    print(y)


def func(array):
    start = 0
    end = len(array)
    width = len(array[0])
    height = len(array)
    first = 0
    second = len(array) - 1

    result = []

    while end - start > 0:
        # one = [array[first][i] for i in range(start, end)]
        one = [array[first][i] for i in range(start, width)]

        if len(one) > 0:
            print(one)
            result.extend(one)

        two = [array[i][second] for i in range(start + 1, height)]
        if len(two) > 0:
            print(two)
            result.extend(two)

        three = [array[second][i] for i in reversed(range(start, width - 1))]
        if len(three) > 0:
            print(three)
            result.extend(three)

        four = [array[i][first] for i in reversed(range(start + 1, height - 1))]
        if len(four) > 0:
            print(four)
            result.extend(four)

        first += 1
        second -= 1

        start += 1
        end -= 1
        width -= 1
        height -= 1

    return result


#  EXAMPLE
[a_05[0][i] for i in range(0, 6)]  # Horizontal
[a_05[i][5] for i in range(1, 6)]  # Vertical

[a_05[5][i] for i in reversed(range(0, 5))]
[a_05[i][0] for i in reversed(range(1, 5))]

[a_05[1][i] for i in range(1, 5)]
[a_05[i][4] for i in range(2, 5)]

[a_05[4][i] for i in reversed(range(1, 4))]
[a_05[i][1] for i in reversed(range(2, 4))]

[a_05[2][i] for i in range(2, 4)]
[a_05[i][3] for i in range(3, 4)]

[a_05[3][i] for i in reversed(range(2, 3))]
[a_05[i][2] for i in reversed(range(3, 3))]  # end

# EXAMPLE 2
[a_005[0][i] for i in range(0, 5)]  # Horizontal left->right
[a_005[i][4] for i in range(1, 6)]  # Vertical down

[a_005[5][i] for i in reversed(range(0, 4))]  # Horizontal right->left
[a_005[i][0] for i in reversed(range(1, 5))]  # Vertical up

[a_005[1][i] for i in range(1, 4)]
[a_005[i][3] for i in range(2, 5)]

[a_005[4][i] for i in reversed(range(1, 4))]
[a_005[i][1] for i in reversed(range(2, 4))]

[a_005[2][i] for i in range(2, 3)]
[a_005[i][2] for i in range(3, 4)]

[a_005[3][i] for i in reversed(range(2, 3))]
[a_005[i][2] for i in reversed(range(3, 3))]  # end


# second -= 1
# start += 1
#
# second == second
# end -= 1
#
# [a_05[1][i] for i in range(1, 3)]
# [a_05[i][2] for i in range(2, 3)]


# def spiral_traverse_01(array: list) -> list:
#     x, y = 0, 0
#     rng = len(array) - 1
#     direction = 1
#
#     while rng > 0:
#         for i in range(len(array[x][y])[::direction]:
#             print(array[x][y][::direction])
#         x += 1
#         while x < rng:
#             print(array[x][y][::direction])
#             x += 1
#         y += direction
#         while y < rng:
#             print(array[x][y])
#             y += 1
#         rng -= 1
#         x = 0
#         direction = -1


if __name__ == '__main__':
    a = a_007
    # spiral_traverse_01(a_01)
    ic(func(a))
