def splitEncode(s):
    for c in s:
        if c not in "#_":
            return "NOT VALID"
    return "".join([chr(96 + len(x)) for x in s.split("_")])
