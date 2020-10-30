from random import random


# finds min element in each step O(n) and adds it into a new array n times. The asymptotic is O(n^2)

def find_smaller(arr):
    """Founds index of the smallest element in the array - O(n)"""
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:  # if current element < previous smallest:
            smallest = arr[i]  # current element in new smallest
            smallest_index = i  # index update

    return smallest_index


def selection_sort(arr):
    """
    Uses find_small(arr) function to add min element every time. Works with O(n^2) asymptotic
    Returns new array and changes the old one
    """
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr.pop(find_smaller(arr)))

    return new_arr


# Let's check ourselves:
a = [int(random() * 100) for i in range(20)]

print(a)
print(selection_sort(a))

print(selection_sort.__doc__)
print(find_smaller.__doc__)