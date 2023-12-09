def sum_of_three(s):
    if len(s) > 9 or "." in s:
        return False
    return int(s) % 3 == 0
