def promotion(x, y, s):
    sumxy = x + y
    return s - (s // sumxy) * y if s % sumxy <= x else (s // sumxy + 1) * x
