def lastDigitDiffZero(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        while ans % 10 == 0:
            ans /= 10
        ans = ans % 100
    return ans % 10
