def count(x):
    res = 0
    mul = 1
    y = x
    while y > 9:
        res += y // 10 * mul if y % 10 > 0 else (y // 10 - 1) * mul + x % mul + 1
        mul *= 10
        y //= 10
    return res


def countZeroDigit(a, b):
    return count(b) - count(a - 1)
