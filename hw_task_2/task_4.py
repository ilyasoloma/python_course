def ListIntersection(_list1, _list2):
    return list(filter(lambda x: x in _list1, _list2))


list1 = [1, 2, 3, 'str']
list2 = ['1', 'str', 3, 2, 4, 5]
print(ListIntersection(list1, list2))
