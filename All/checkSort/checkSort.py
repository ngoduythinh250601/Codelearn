def checkSort(a):
    s = set()
    s.add(a[0])
    for i in range(1, len(a)):
        if a[i] != a[i - 1]:
            if a[i] in s:
                return False
            s.add(a[i])
    return True
