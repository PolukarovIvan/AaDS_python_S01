def binary_search(lst, item):
    # simple binary search implementation
    low = 0  # lower bound
    high = len(lst) - 1  # upper bound

    while low <= high:  # while you haven't narrow it into one element:
        mid = (low + high) // 2  # calculate the middle
        guess = lst[mid]  # check the middle element
        if guess == item:  # if we guessed
            return mid
        elif guess > item:  # if our item is less than the middle:
            high = mid - 1  # change upper bound to the middle
        else:  # if our item is more than middle element:
            low = mid + 1  # change lower bound to the middle
    # if we haven't found current element:
    return None


lst = [1, 2, 45, 342, 545, 1233, 10000]

print(binary_search(lst, 545))  # Output: 4
print(binary_search(lst, 546))  # Output: None
