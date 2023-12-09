def baseChange(num, base):
    if num == 0:
        return 0
    ans = []
    while num > 0:
        ans.append(str(num % base))
        num //= base
    return int("".join(ans[::-1]))
