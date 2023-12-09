def removeDuplicateCharacters(str):
    return "".join(c if str.count(c) == 1 else "" for c in str)
