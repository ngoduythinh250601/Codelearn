def countNumber(arr, l, r):
    from math import gcd

    lcms = arr[0]
    for i in range(1, len(arr)):
        lcms = lcms * arr[i] // gcd(lcms, arr[i])
    if lcms == 0:
        return 0
    return r // lcms - (l - 1) // lcms
