def Multiples(_num):
    numList = [10, 2, 5, 3, 21, 4]
    return list(filter(lambda x: x % num == 0, numList))

num = 2
print(Multiples(num))
