"""
Non-constructible Change
Given an array of positive integers representing the values of coins in your possession,
write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create. The
given coins can have any positive integer value and aren’t necessarily unique(i.e., you can have multiple coins of
the same value). For example, if you’re given coins = [1,2,5], the minimum amount of change that you can’t create is
4. If you’re given no coins, the minimum amount of change that you can’t create is 1.
"""

from icecream import ic

coins = [[5, 7, 1, 1, 2, 3, 22], [], [1, 1, 1, 1, 1], [1, 5, 1, 1, 1, 10, 15, 20, 100], [1, 2, 3, 7], [1, 1, 3, 7],
         [1, 2, 5], [1, 1, 1, 1, 1], [5, 6, 1, 1, 2, 3, 4, 9], [1, 1], [1], [1, 2, 3, 4, 5, 6, 7]]

seven = [5, 6, 1, 1, 2, 3, 4, 9]
nine = [1, 1]
_10 = [2]  # 1
_11 = [1]
_4 = [6, 4, 5, 1, 1, 8, 9]  # 3
_5 = []  # 1

# THEIR solution: pay attention to returns, breaks are not needed when returning from IF, for e.g.!
# O(nlogn) time | O(1) space where n is the number of the coins
def nonConstructibleChange(coins):
    coins.sort()
    r_total = 0
    for c in coins:
        if c > r_total + 1:
            return r_total + 1
        r_total += c
    return r_total + 1


def non_constructible_change(c):
    if len(c) == 0:
        return 1
    c.sort()
    running_total = 0
    for idx, coin in enumerate(range(len(c))):
        coin_value = c[idx]
        diff = coin_value - running_total
        if diff > 1:
            running_total += 1
            break
        else:
            running_total += coin_value
    if not diff > 1:
        running_total += 1
    return running_total


if __name__ == '__main__':
    coins = _5
    coins.sort()
    print(non_constructible_change(coins))
