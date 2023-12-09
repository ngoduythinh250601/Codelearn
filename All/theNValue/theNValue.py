def theNValue(n):
    if n < 0:
        return 0
    ans = list(str(n))
    for i in range(1, len(ans)):
        ans[i] = str((int(ans[i]) + 1) % 10)
    return int("".join(ans))
