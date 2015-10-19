def MAKE_SET(x):
    x.p = x
    x.rank = 0

def UNION(x, y):
    _LINK(FIND_SET(x), FIND_SET(y))

def _LINK(x, y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank==y.rank:
            y.rank += 1

def FIND_SET(x):
    if x!=x.p:
        x.p = FIND_SET(x.p)
    return x.p

