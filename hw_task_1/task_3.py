from random import randint
def addCustomValue(ls):
    ls.append(randint(-100, 100))
    return ls

list =  [1,2,3,4,322,23]
print(addCustomValue(list))