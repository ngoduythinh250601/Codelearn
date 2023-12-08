def primeXor(a, b):
    ans = 1
    for i in range(2, int(max(a, b) ** 0.5) + 1):
        c1, c2 = 0, 0
        while a % i == 0:
            c1, a = c1 + 1, a / i
        while b % i == 0:
            c2, b = c2 + 1, b / i
        if (c1 == 0 or c2 == 0) and c1 + c2 > 0:
            ans *= i
    if a == b:
        return ans
    if a > 1:
        ans *= a
    if b > 1:
        ans *= b
    return ans
