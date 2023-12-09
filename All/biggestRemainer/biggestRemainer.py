def biggestRemainer(arr):
    a = list(set(arr))
    a.sort()
    return a[-2] if len(a) > 1 else 0
