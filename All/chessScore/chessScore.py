def chessScore(arr):
    d = {"t": 1, "M": 3, "T": 3, "X": 5, "H": 9, "V": 0}
    return sum(d[i] for i in arr)
