def root(n):
    if n < 10:
        return n
    return root(sum([int(x) for x in str(n)]))
