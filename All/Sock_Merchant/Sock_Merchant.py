def sock_merchant(sizes):
    sizes.sort()
    sizes.append(-1)
    ans, count = 0, 1
    for i in range(1, len(sizes)):
        if sizes[i] == sizes[i - 1]:
            count += 1
        else:
            ans += count // 2
            count = 1
    return ans
