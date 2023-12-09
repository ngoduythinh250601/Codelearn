def longestCommonPrefix(array):
    if len(array) == 0:
        return ""
    d, c = 0, min([len(s) for s in array])
    while d < c:
        mid = (d + c) // 2 + 1
        oke, pref = True, array[0][:mid]
        for s in array:
            if not s.startswith(pref):
                oke = False
                break
        if oke:
            d = mid
        else:
            c = mid - 1
    return array[0][:d]
