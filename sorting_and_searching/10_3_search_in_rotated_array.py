# 10.3 Search in Rotated Array
# ==============================================================================================
# Given a sorted array of n integers that has been rotated an unknown number of times, write
# code to find an element in the array. You may assume that the array was originally sorted in
# increasing order.
# ==============================================================================================
def search_rotated(array, target, low, high):
    if low <= high:
        mid = (low + high) / 2
        if target == array[mid]:
            return mid  # found it, yay!
        # now look for which half is normally sorted?
        if array[low] < array[mid]:  # left is normal
            if target > array[low] and target < array[mid]:
                return search_rotated(array, target, low, mid - 1)
            else:
                return search_rotated(array, target, mid + 1, high)

        elif array[low] > array[mid]:  # right is normal
            if target > array[mid] and target < array[high]:  # target in betwee
                return search_rotated(array, target, mid + 1, high)
            else:
                return search_rotated(array, target, low, mid - 1)

        elif array[low] == array[mid]:
            if array[mid] != array[high]:
                return search_rotated(array, target, mid + 1, high)
            else:
                result = search_rotated(array, target, low, mid - 1)
                if result == -1:
                    return search_rotated(array, target, mid + 1, high)
                return result
    return -1


rotated = [10, 15, 20, 0, 5]
print search_rotated(rotated, 5, 0, len(rotated) - 1)