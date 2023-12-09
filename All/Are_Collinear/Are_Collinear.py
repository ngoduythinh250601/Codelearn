def collinear(coordinates):
    x, y, z = coordinates
    return (z[1] - x[1]) * (y[0] - x[0]) == (y[1] - x[1]) * (z[0] - x[0])
