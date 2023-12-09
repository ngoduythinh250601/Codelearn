def need_money(t, s, p):
    from math import ceil, log

    return ceil(log(t / s, 1 + p / 100))
