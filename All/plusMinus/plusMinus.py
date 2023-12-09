def plus_minus(arr):
    leng = len(arr)
    p = round(sum(i > 0 for i in arr) / leng, 6)
    n = round(sum(i < 0 for i in arr) / leng, 6)
    z = round(sum(i == 0 for i in arr) / leng, 6)
    return [p, n, z]
