def leastNumOfCubes(n):
    dd = [n + 1] * (n + 1)
    dd[0] = 0
    for i in range(n):
        j, tmp = 1, 1
        while i + tmp <= n:
            dd[i + tmp] = min(dd[i + tmp], dd[i] + 1)
            j += 1
            tmp = j**3
    return dd[n]
