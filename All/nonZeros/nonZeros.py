def rz(x):
    return int(str(x).replace("0", ""))


def nonZeros(v, a):
    return "YES" if rz(v) + rz(a) == rz(v + a) else "NO"
