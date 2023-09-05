def decore(fn):
    def wrapper(n):
        try:
            result = fn(n) / 4
            return result
        except TypeError as e:
            print(f'Повторный вызов функции из-за ошибки: {e}')
            return fn(n)
    return wrapper

@decore
def fun(n):
    return n
@decore
def funEx(n):
    return str(n)

#print(fun(4))
print(funEx(4))