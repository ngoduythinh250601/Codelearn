def pretty_array(arr):
    odds = sum(v % 2 == 1 for v in arr)
    return min(len(arr) - odds, odds)
