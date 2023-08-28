def getAcronym(string):
    try:
        string = string.split()
        tmp = ''
        for word in string:
            tmp += word[0]
        return tmp.upper()
    except (TypeError, AttributeError) as ex:
        print(f'Полученная переменная не является строкой.\n Подробнее: {ex}')

print(getAcronym("dsds ere htht ее"))