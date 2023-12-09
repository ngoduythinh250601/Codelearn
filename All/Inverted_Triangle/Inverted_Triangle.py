def verticesValue(edge):
    while len(edge) != 1:
        edge = [edge[i] - edge[i - 1] for i in range(1, len(edge))]
    return str(edge[0] % -1000000007) if edge[0] < 0 else str(edge[0] % 1000000007)
