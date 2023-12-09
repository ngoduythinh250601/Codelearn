def goodDivisorNumber(n):
    u = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            u.append(i)
            if i * i < n:
                u.append(n // i)
    u.sort()
    for i in range(1, len(u)):
        if n % (u[i] - u[i - 1]) != 0:
            return False
    return True
