import math


def rec_sum(arr):
    if not arr:
        return 0
    return arr[0] + rec_sum(arr[1:])


print(rec_sum([1, 2, 3, 4, 5]))


def rec_size(arr):
    if not arr:
        return 0
    else:
        return 1 + rec_size(arr[1::])


print(rec_size([1, 2, 3, 4]))


def rec_maximum(arr):
    if not arr:
        return -1
    else:
        return max(arr[0], rec_maximum(arr[1::]))


print(rec_maximum([1, 2, 3, 4]))