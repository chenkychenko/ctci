# 10.4 Sorted Search, No Size
# ==============================================================================================
# You are given an array-like data structure Listy which lacks a size method. It does, however,
# have an element_at(i) method that returns the element at index i in O(1) time. If i is beyond
# the bounds of the data structure, it returns -1. (For this reason, the data structure only
# supports positive integers.) Given a Listy which contains sorted, positive integers, find the
# index at which an element x occurs. If x occurs multiple times, you may return any index.
# ==============================================================================================
def search_listy_helper(listy, target):
    index = 1
    while listy[index] != -1 and listy[index] < target:
        index *= 2
    return search_listy(listy, target, index / 2, index)


def search_listy(array, target, low, high):
    if high < low:
        return -1  # base case - not found
    mid = (low + high) / 2
    if array[mid] == target:
        return mid  # found it, returning index
    elif array[mid] == -1 or target < array[mid]:  # search left side
        return search_listy(array, target, low, mid - 1)
    else:
        return search_listy(array, target, mid + 1, high)