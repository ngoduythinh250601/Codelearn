def digitsProduct(product):
    if product == 0:
        return 10
    if product == 1:
        return 1
    ans = []
    for i in range(9, 1, -1):
        while product % i == 0:
            ans.append(str(i))
            product /= i
    return int("".join(ans)[::-1]) if product == 1 else -1
