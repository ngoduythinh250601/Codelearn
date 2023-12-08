def arrayChange(a):
    ans, current = 0, a[0] - 1
    for x in a:
        if x > current:
            current = x
        else:
            ans += current - x + 1
            current += 1
    return ans
