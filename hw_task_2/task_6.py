def decore(fn):
    def wrapper(n):
        result = fn(n)
        if type(result) != int:
            raise TypeError("Only int")
        else:
            return result
    return wrapper

@decore
def fun(n):
    return n
@decore
def funEx(n):
    return str(n)

print(fun(4))
print(funEx(4))