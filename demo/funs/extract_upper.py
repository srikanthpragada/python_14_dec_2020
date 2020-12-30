
def upper(st):
    chars = []
    for ch in st:
        if ch.isupper():
            chars.append(ch)

    return ''.join(chars)


def getupper(st):
    nst = ""
    for ch in st:
        if ch.isupper():
            nst += ch

    return nst


print(upper('AbcXyz'), getupper('AbcXyz'))
