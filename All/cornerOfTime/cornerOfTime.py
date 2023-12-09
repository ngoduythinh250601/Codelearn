def corner_of_time(h, m):
    from math import ceil

    ans = abs(30 * (h % 12) + 0.5 * m - 6 * m)
    return min(ceil(ans), ceil(360 - ans))
