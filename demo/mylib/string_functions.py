def hasupper(s):
    for c in s:
        if c.isupper():
            return True

    return False


def hasdigit(s):
    for c in s:
        if c.isdigit():
            return True

    return False
