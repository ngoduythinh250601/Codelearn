def isPronic(n):
    if n == 0:
        return True
    return int(n**0.5) * (int(n**0.5) + 1) == n
