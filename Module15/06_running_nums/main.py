def cyclic_shift_right(lst, k):
    n = len(lst)
    k %= n
    lst[:] = lst[-k:] + lst[:-k]
    return lst

# Примеры использования
lst1 = [1, 2, 3, 4, 5]
k1 = 1
print("Изначальный список:", lst1)
print("Сдвинутый список:", cyclic_shift_right(lst1, k1))

lst2 = [1, 4, -3, 0, 10]
k2 = 3
print("\nИзначальный список:", lst2)
print("Сдвинутый список:", cyclic_shift_right(lst2, k2))
