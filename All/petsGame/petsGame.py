def pets_game(x, y):
    from math import log

    a, b = y * log(x), x * log(y)
    return 1 if a > b else 0 if a == b else -1
