def flipColor(color, t):
    n, m = len(color), len(t)
    t.sort(reverse=True)
    j = 0
    for i in range(n - 1, -1, -1):
        color[i] = (color[i] + m - j) % 2
        while j < m and t[j] == i:
            j += 1
    return color
