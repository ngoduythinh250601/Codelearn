def fromDecimal(b, n):
    ans = []
    while n > 0:
        ans.append(str(n % b))
        n //= b
    return "".join(ans)[::-1]
