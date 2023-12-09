def numberOfCombinations(n, k):
    from math import factorial as f

    return f(n) // f(k) // f(n - k)
