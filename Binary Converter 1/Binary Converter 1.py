def text_to_binary(text):
    return " ".join("{0:08b}".format(ord(c)) for c in text)
