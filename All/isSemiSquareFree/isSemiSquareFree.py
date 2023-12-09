def isSemiSquareFree(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        d = 0
        while n % i == 0:
            d += 1
            n //= i
        if d > 0 and d % 2 == 0:
            return False
    return True
