def regionCount(s):
    spec = "QROPAD"
    return sum([2 if c in spec else 3 if c == "B" else 1 for c in s])
