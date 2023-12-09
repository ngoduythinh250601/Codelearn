def amaranthus(n, lst):
    s = list(set(lst))
    s.sort(reverse=True)
    return f"1st : {lst.count(s[0])}; 2nd : {lst.count(s[1])}; 3rd : {lst.count(s[2])}"
