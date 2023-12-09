def evenSubStrings(s):
    return sum([i + 1 if int(s[i]) % 2 == 0 else 0 for i in range(len(s))])
