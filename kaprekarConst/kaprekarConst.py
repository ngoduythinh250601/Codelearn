def kaprekarConst(n):
    ans = 0
    while True:
        digits = [int(d) for d in str(n)]
        while len(digits) < 4:
            digits.append(0)
        digits = sorted(digits)
        bigger = digits[3] * 1000 + digits[2] * 100 + digits[1] * 10 + digits[0]
        smaller = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]
        ans += 1
        n = bigger - smaller
        if n == 0:
            return 0
        if n == 6174:
            return ans
