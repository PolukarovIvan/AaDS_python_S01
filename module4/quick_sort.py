import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([int(random.random() * 10000) for i in range(10000, 0, -1)]))


def merge_sort(arr, operations=0):
    length = len(arr)
    if length <= 1:
        return arr, 1
    pivot_index = length // 2
    greater = [i for i in arr if i >= arr[pivot_index]]
    less = [i for i in arr if i < arr[pivot_index]]

    return quick_sort(less) + quick_sort(greater),


print(merge_sort(list(range(10))))
