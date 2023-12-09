def christmasTree(levelNum, levelHeight):
    num, ans = [1, 1, 3], []
    for iNum in range(levelNum):
        cnt = 5 + iNum * 2
        for ite in range(levelHeight):
            num.append(cnt)
            cnt += 2
    for i in range(levelNum):
        num.append(levelHeight if levelHeight % 2 == 1 else levelHeight + 1)
    maxSpace = max(num) // 2
    for x in num:
        ans.append(" " * (maxSpace - x // 2) + "*" * x)
    return ans
