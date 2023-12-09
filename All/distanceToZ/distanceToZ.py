def distanceToZ(a):
    return "".join([chr(122 - v) if v != -1 else " " for v in a])
