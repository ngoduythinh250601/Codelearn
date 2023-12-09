def sumOfDivisor(n):
    res = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            res += i + (n // i)
        if i * i == n:
            res -= i
    return res


def redundancy_number(n):
    if n <= 0:
        return n
    while sumOfDivisor(n) <= n:
        n += 1
    return n
