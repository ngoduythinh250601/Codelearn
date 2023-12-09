def square_included(n):
    if n <= 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % (i**2) == 0:
            return True
    return False
