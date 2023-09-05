from time import time
def MeasureTime(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {execution_time} секунд")
        return result
    return wrapper

@MeasureTime
def Fibonacci(n):
    fib1 = fib2 = 1
    if n in (1, 2):
        return 1
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2

@MeasureTime
def Collatz(n):
    answer = []
    answer.append(n)
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n +1
        answer.append(int(n))
    return answer

print(Fibonacci(10000))
print(Collatz(11000))
