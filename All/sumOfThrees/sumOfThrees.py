def sumOfThrees(n):
    ni = int(n)
    m, ans, i = 0, [], 0
    while ni > 0:
        tmp = ni % 3
        if tmp == 2:
            return "Impossible"
        elif tmp == 1:
            ans.append("3^" + str(i))
        i += 1
        ni //= 3
    return "+".join(ans[::-1])
