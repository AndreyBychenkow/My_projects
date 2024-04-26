def partition(lst):
    pivot = lst[-1]
    less = []
    equal = []
    greater = []

    for item in lst:
        if item < pivot:
            less.append(item)
        elif item == pivot:
            equal.append(item)
        else:
            greater.append(item)

    return less, equal, greater


def quicksort(lst):
    if len(lst) <= 1:
        return lst

    less, equal, greater = partition(lst)

    sorted_less = quicksort(less)
    sorted_greater = quicksort(greater)

    return sorted_less + equal + sorted_greater


numbers = [4, 9, 2, 7, 5]
print(partition(numbers))
print(quicksort(numbers))
