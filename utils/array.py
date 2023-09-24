def checkArrayLengths(*args) -> bool:
    lengths = [len(arg) for arg in args]

    if len(set(lengths)) != 1:
        return False

    return True
