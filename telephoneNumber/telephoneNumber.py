def telephoneNumber(s):
    return "YES" if s.find("8") != -1 and len(s) - s.find("8") >= 11 else "NO"
