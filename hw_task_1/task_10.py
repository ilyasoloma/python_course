# Не до конца понял условие, поэтому предлагаю 2 варианта решения:
# 1. С применением цикла while;
# 2. С применением альтернативного варианта конструкции цикла for.

# Также, в эталонном решении, функция print находится внутри цикла,
# что приведет к выводу списка на каждом шаге, хотя в комментарии
# с результатом указан список, получаемый по окончанию выполнения кода.
# Мое решение соответствует комментарию.


lst = [2, 4, 5, 8, 9, 13]
index = 0
while index < len(lst):
    lst[index] *= index
    index += 1
print(f'Решение с применением while: {lst}')

lst = [2, 4, 5, 8, 9, 13]
lst = [num * index for index, num in enumerate(lst)]
print(f'Решение с применением альтернативного вариатнта конструкции цикла for: {lst}')