dd = [[-1] * 2001 for i in range(2001)]


def water(h, a):
    if dd[h][a] > -1:
        return dd[h][a]
    res = 0
    if h > 5 and a > 10:
        res = water(h - 2, a - 8) + 2
    if h > 20:
        res = max(res, water(h - 17, a + 7) + 2)
    dd[h][a] = res
    return res


def dieHard(h, a):
    return water(h + 3, a + 2) + 1
