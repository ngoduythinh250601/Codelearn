def reverse_prime(L, R):
    nt = []
    dd = [0] * 10000005
    for i in range(2, 10000001):
        if dd[i] == 0:
            nt.append(int(str(i)[::-1]))
            for j in range(i * i, 10000001, i):
                dd[j] = 1
    nt.sort()
    x, y = 0, len(nt)
    for i in range(len(nt)):
        if nt[i] >= L:
            x = i
            break
    if nt[x] > R:
        return []
    for i in range(x, len(nt)):
        if nt[i] > R:
            y = i
            break
    return nt[x:y]
