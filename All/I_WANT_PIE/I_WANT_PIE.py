def lots_of_pie(n, k):
    from math import factorial as f

    try:
        return str(f(n) // f(k) // f(n - k))
    except:
        return "-1"
