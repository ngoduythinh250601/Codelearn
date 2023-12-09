def isSquareFreeInteger(n):
    for i in range(2, int(n**0.5) + 1):
        cnt = 0
        while n % i == 0:
            n //= i
            cnt += 1
        if cnt > 1:
            return False
    return True
