def sum_of_cubes_odd_number(n):
    if n <= 0:
        return -1
    base = int(1e9 + 7)
    return (n**2 * (2 * n**2 - 1)) % base
