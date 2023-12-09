def specialPolynomial(x, n):
    if x == 1:
        return n - 1
    cr, k, total = 1, 0, 1
    while total <= n:
        k += 1
        cr *= x
        total += cr
    return k - 1
