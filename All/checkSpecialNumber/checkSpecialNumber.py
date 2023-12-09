def check_special_number(n):
    return len(str(n)) == len(set(str(n)))
