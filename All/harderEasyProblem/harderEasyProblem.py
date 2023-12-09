def harderEasyProblem(p, q, r):
    ans = []
    for i in range(len(p)):
        if q[i] != 0:
            y = int((-r[i] + (r[i] ** 2 + 4 * q[i] * p[i]) ** 0.5) / (2 * q[i]))
        else:
            y = p[i] // r[i]
        ans.append([q[i] * y + r[i], y])
    return ans
