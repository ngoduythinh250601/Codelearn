def squaredDivided(n):
    import math

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % (i * i) == 0:
            return False
    return True
