def findRange(array, n):
    s, d = 0, 0
    for i in range(len(array)):
        s += array[i]
        while s > n:
            s -= array[d]
            d += 1
        if s == n and d <= i:
            return True
    return False
