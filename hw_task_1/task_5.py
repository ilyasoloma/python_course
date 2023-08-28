def checkContent(s1, s2):
    if s2.find(s1) != -1:
        print('ДА')
    else:
        print('НЕТ')

str_1 = 'test'
str_2 = 'test1'
checkContent(str_1, str_2)