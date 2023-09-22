def checkArrayLengths(*args):
    lengths = [len(arg) for arg in args]

    if len(set(lengths)) != 1:
        raise ValueError("Arrays have different lengths: %s" % lengths)

    return True
