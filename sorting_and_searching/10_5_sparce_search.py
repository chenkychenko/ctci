# 10.5 Sparce Search
# ==============================================================================================
# Given a sorted array of strings that is interspersed with empty strings, write a method to find
# the location of a given string.
# ==============================================================================================
def sparce_search_helper(array, target):
    return sparce_search(array, target, 0, len(array)-1)

def sparce_search(array, target, low, high):
    if low <= high:
        mid = (low+high)/2
        if array[mid] == target:
            return mid # found it! return index
        if array[mid] == "": # found empty string, go left and right until encounter value
            offset = 1
            while not array[mid-offset] and not array[mid+offset]:
                offset += 1
            mid = mid-offset if array[mid-offset] else mid+offset
            if array[mid]: # found value, let's compare
                if target == array[mid]:
                    return mid
                elif target < array[mid]:
                    return sparce_search(array, target, low, mid-1)
                else:
                    return space_search(array, target, mid+1, high)
    return -1 # not found

sparce_array = ["at","","","","ball","","","car","","","dad","",""]
print sparce_search_helper(sparce_array, "car")