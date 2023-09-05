def FindStr(*args):
    return tuple(filter(lambda x: isinstance(x, str), args))


print(FindStr(1321, 54534, '123', 'test'))
