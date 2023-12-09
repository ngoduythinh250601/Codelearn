def nextPowerOfTwo(n):
    ans = 2 ** int(math.log2(n))
    return ans * (1 if ans == n else 2)
