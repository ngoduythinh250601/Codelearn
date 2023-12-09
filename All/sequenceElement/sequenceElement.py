base = (
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1],
)


def dot(x, y):
    res = [[0] * 5 for i in range(5)]
    for i in range(5):
        for j in range(5):
            for k in range(5):
                res[i][j] += x[i][k] * y[k][j]
            res[i][j] %= 10
    return res


def calc(n):
    if n == 1:
        return base
    x = calc(n // 2)
    x = dot(x, x)
    return x if n % 2 == 0 else dot(x, base)


def sequenceElement(a, n):
    if n == 0:
        return a[0]
    mt = calc(n)
    ans = 0
    for i in range(5):
        ans += a[i] * mt[i][0]
    return ans % 10


# def nextseq(x):
#     x.append(sum(x)%10)
#     x.pop(0)
#     return x

# def sequenceElement(a,n):
#     tho, rua, ld= a.copy(), a.copy(), 0
#     while True:
#         tho = nextseq(nextseq(tho))
#         rua = nextseq(rua)
#         if tho==rua: break
#     tho = a
#     while tho!=rua:
#         if n==0: return tho[0]
#         tho = nextseq(tho)
#         rua = nextseq(rua)
#         n-=1
#     while True:
#         tho = nextseq(tho)
#         ld+=1
#         if tho==rua: break
#     n %= ld
#     for i in range(n):
#         tho = nextseq(tho)
#     return tho[0]
