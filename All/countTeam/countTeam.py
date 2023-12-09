def countTeam(s):
    n = int(s, 2)
    return "even" if (n * (n - 1) * (n - 2) // 6) % 2 == 0 else "odd"
