def counterPoN(l, r, k):
    from math import ceil, floor

    ans = 0
    for i in range(ceil(l ** (1 / 2)), floor(r ** (1 / 2)) + 1):
        for j in range(ceil(l ** (1 / 3)), floor(r ** (1 / 3)) + 1):
            print(i, j)
            if abs(i**2 - j**3) <= k:
                ans += 1
    return ans
