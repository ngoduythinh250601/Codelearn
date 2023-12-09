def make_flags(k, n):
    from math import factorial as f

    return f(n) // f(k) // f(n - k)
