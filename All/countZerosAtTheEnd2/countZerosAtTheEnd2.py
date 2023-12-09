def countZerosAtTheEnd2(n):
    if n % 2 == 1:
        return 0
    n //= 2
    ans = 0
    while n > 0:
        ans += n // 5
        n //= 5
    return ans
