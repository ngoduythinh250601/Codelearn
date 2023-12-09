def min_number_array(a):
    for i in range(len(a) + 1):
        if i not in a:
            return i
