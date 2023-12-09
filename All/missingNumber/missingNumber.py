def missingNumber(arr):
    for i, x in enumerate(sorted(arr)):
        if x != i + 1:
            return i + 1
    return len(arr) + 1
