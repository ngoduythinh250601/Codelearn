def countPerfectTeam(a, b, c):
    return min(a, b, (a + b + c) // 3)
