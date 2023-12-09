def pairOfShoes(shoes):
    l, r = [], []
    for p in shoes:
        if p[0] == 0:
            l.append(p[1])
        else:
            r.append(p[1])
    l.sort()
    r.sort()
    return l == r
