def max_product(A):
    b = sorted(A)
    return max(b[0] * b[1], b[-1] * b[-2])
