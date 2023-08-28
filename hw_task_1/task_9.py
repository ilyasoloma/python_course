from math import prod
def factorial(num):
    return prod(i for i in range(1, num+1))

print(factorial(6))