def sum_extended(*args):
    total = 0
    for arg in args:
        if isinstance(arg, list):
            total += sum_extended(*arg)
        else:
            total += arg
    return total


# print(sum_extended([[1, 2, [3]], [1], 3]))
# print(sum_extended(1, 2, 3, 4, 5))
