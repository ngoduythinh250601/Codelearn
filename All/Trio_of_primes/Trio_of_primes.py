def prime(m):
    mark = [True] * (m + 1)
    mark[0] = mark[1] = False
    p = []
    for i in range(2, m + 1):
        if mark[i]:
            j = i * i
            while j <= m:
                mark[j] = False
                j += i
            p.append(i)
    return p, mark, len(p)


def trio_of_primes(n):
    p, mark, s = prime(n)
    ans = []
    for i in range(s):
        pi = p[i]
        for j in range(i, s):
            pj = p[j]
            if pi + pj + pj > n:
                break
            if mark[n - pi - pj]:
                ans.append([pi, pj, n - pi - pj])
    if ans == []:
        ans.append([-1])
    return ans
