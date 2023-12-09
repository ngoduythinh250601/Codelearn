def stringXor(s, t):
    a = [int(c) for c in s]
    b = [int(c) for c in t]
    ans = []
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 or j >= 0:
        x1 = a[i] if i >= 0 else 0
        x2 = b[j] if j >= 0 else 0
        ans.append(x1 ^ x2)
        i -= 1
        j -= 1
    return ("".join([str(x) for x in ans]))[::-1]
