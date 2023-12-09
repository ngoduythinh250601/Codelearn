def longestCommonPrefix(array):
    if len(array) == 0:
        return ""
    for i in range(len(array[0])):
        for j in range(1, len(array)):
            if array[0][i] != array[j][i]:
                return array[0][:i]
    return array[0]
