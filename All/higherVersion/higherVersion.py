def higherVersion(v1, v2):
    return [int(x) for x in v1.split(".")] > [int(x) for x in v2.split(".")]
