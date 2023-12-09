def stringTask2(str):
    str = str.lower()
    for char in "aoyeui":
        str = str.replace(char, "")
    return "." + ".".join(list(str)) if len(str) > 0 else ""
