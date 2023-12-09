def is_pangram(s):
    return set(s.lower()) >= set("abcdefghijklmnopqrstuvwxyz")
