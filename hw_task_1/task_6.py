def countPositiveNum(ls):
    return sum(i > 0 for i in ls)
list = [-1,-2, 3,-4,-5]
print(countPositiveNum(list))