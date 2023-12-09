def calculateElectricBill(n):
    ans = 1000
    rule = [[50, 230], [50, 480], [49, 700], [1000000, 900]]
    for r in rule:
        if n > r[0]:
            ans += r[0] * r[1]
            n -= r[0]
        else:
            ans += n * r[1]
            break
    return ans
