def arePermutation(str1, str2):
    if len(str1) != len(str2):
        return 0
    count1 = [0] * 256
    count2 = [0] * 256
    for i in str1:
        count1[ord(i)] += 1
    for i in str2:
        count2[ord(i)] += 1
    for i in range(256):
        if count1[i] != count2[i]:
            return 0
    return 1


def swapSwap(a, b):
    if arePermutation(a, b) == 0:
        return -1
    cnt = 0
    for i in range(len(a)):
        cnt += 0 if a[i] == b[i] else 1
    return (cnt + 1) // 2
