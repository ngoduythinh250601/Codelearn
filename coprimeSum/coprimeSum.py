def coprimeSum(n):
    import math

    ans = 0
    for i in range(1, n + 1):
        if math.gcd(i, n) == 1:
            ans += i
    return ans
