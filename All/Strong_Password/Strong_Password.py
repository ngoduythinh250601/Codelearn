def strong_pass(password):
    spec = "!@#$%^&*()-+"
    a, b, c, d = 0, 0, 0, 0
    for ch in password:
        if ch in spec:
            a = 1
        if ch.islower():
            b = 1
        if ch.isupper():
            c = 1
        if ch.isnumeric():
            d = 1
    ans = max(6 - len(password), 4 - a - b - c - d)
    return ans if ans > 0 else -1
