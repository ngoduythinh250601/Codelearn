def EuclidDistance(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def isSquare(x, y):
    d = []
    for i in range(4):
        for j in range(i + 1, 4):
            d.append(EuclidDistance(x[i], y[i], x[j], y[j]))
    d.sort()
    return d[0] == d[3] and d[4] == d[5] and d[0] * 2 == d[4]
