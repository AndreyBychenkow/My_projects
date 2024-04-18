def tpl_sort(tpl):
    if all(isinstance(x, int) for x in tpl):
        return tuple(sorted(tpl))
    else:
        return tpl

# tpl = (6, "a", -1, 8, 4, 10, -5)
# print(tpl_sort(tpl))

# На просторах интернета нашел вот такую интересную встроенную функцию
# isinstance(x, int) , которая проверяет, является ли объект x указанного класса
# (в нашем случае int). Если x является целым числом, функция возвращает True, иначе False.
