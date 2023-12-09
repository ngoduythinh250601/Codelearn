def collect(a, b):
    if a < 2:
        a = 2
    if b < 2:
        b = 2
    from math import sqrt, ceil, floor

    ans = []
    for i in range(ceil(sqrt(a)), floor(sqrt(b)) + 1):
        check = True
        for j in range(2, floor(sqrt(i)) + 1):
            if i % j == 0:
                check = False
                break
        if check == True:
            ans.append(i * i)
    return ans if len(ans) > 0 else [-1]
