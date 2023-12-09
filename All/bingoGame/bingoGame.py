def bingoGame(a,b):
    for index in range(25):
        arr = b[:index+1]
        # rows
        for row in a:
            cnt = 0
            for box in row:
                cnt += 1 if box in arr else 0
            if cnt == 5:
                return index
        # cols
        for i in range(5):
            col = []
            for j in range(5): col.append(a[j][i])

            print(col)
            cnt = 0
            for box in col:
                cnt += 1 if box in arr else 0
            if cnt == 5:
                return index
        # 2 diagonal line
        cnt = 0
        for i in range(5):
            cnt += 1 if a[i][i] in arr else 0
        if cnt == 5: return index

        cnt = 0
        for i in range(5):
            cnt += 1 if a[i][4 - i] in arr else 0
        if cnt == 5: return index   