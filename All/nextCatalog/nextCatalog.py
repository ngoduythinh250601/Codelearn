def nextCatalog(s, k):
    existed_char = sorted(set(s))
    d = dict(zip(existed_char, range(len(existed_char))))
    if k > len(s):
        return s + existed_char[0] * (k - len(s))
    arr = [d[c] for c in s[:k]]
    base = len(existed_char)
    # to decimal
    dcm = 0
    for value in arr:
        dcm = dcm * base + value
    dcm += 1
    # to base-mal
    for i in range(len(arr) - 1, -1, -1):
        arr[i] = dcm % base
        dcm //= base
    return "".join([existed_char[i] for i in arr])
