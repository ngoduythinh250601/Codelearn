def goldRush(arr):
    if len(arr) == 0:
        return True
    return len(arr) == 1 or max(arr) != min(arr)
