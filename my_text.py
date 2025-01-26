def counter(text):
    words = text.split()
    return len(words)


def longotshort(text):
    words = text.split()
    return sorted(words, key=len, reverse=True)


def alph(text):
    words = text.split()
    return sorted(words)
