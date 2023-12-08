def setOddBits(n):
    if n == 0:
        return 0
    a = list("{:b}".format(n))
    for i in range(len(a) - 1, -1, -2):
        a[i] = "1"
    return int("".join(a), 2)
