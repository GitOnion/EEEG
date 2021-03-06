from itertools import izip_longest


def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> 'ABC' 'DEF' 'Gxx'"
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)
