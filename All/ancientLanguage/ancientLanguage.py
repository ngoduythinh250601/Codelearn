def ancientLanguage(s):
    n = len(s)
    a, b, c = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        a[i] = a[i + 1] + (1 if s[i] == "W" else 0)
    for i in range(n - 1, -1, -1):
        b[i] = b[i + 1] + (a[i + 1] if s[i] == "O" else 0)
    for i in range(n - 1, -1, -1):
        c[i] = c[i + 1] + (b[i + 1] if s[i] == "C" else 0)
    return c[0]
