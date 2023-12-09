def gcdOfNumbers(a):
    import math

    ans = a[0]
    for i in a:
        ans = math.gcd(i, ans)
    return ans
