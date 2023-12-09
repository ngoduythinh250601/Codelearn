def beautifulNumbers(n):
    s = str(n)
    return 1 + (len(s) - 1) * 9 + int(s[0]) - (1 if s[0] * len(s) > s else 0)
