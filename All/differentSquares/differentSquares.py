def differentSquares(matrix):
    dif = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            item = [
                matrix[i][j],
                matrix[i][j + 1],
                matrix[i + 1][j],
                matrix[i + 1][j + 1],
            ]
            if item not in dif:
                dif.append(item)
    return len(dif)
