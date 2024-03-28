lst = [6, 4, -8, 2, 15]
print("Изначальный список:", lst)

for i in range(len(lst)):
    mini = i
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[mini]:
            mini = j
    lst[i], lst[mini] = lst[mini], lst[i]

print("Отсортированный список:", lst)
