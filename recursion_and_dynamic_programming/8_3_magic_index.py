# 8.3 Magic Index
# ==============================================================================================
# A magic index in an array A[0-N-1] is defined to be an index such that A[i] = i. Given a sorted
# array of distinct integers, write a method to find a magic index, if one exists, in array A.
# ==============================================================================================
def find_magic_index(array, start, end):
    if end <= start:
        return -1 # error
    midpoint = (start + end) / 2
    if array[midpoint] == midpoint:
        return midpoint # found magic index!
    if array[midpoint] > midpoint: # search left
        return find_magic_index(array, start, midpoint-1)
    return find_magic_index(array, midpoint+1, end)

my_array = [0, 3, 8, 9, 10]
res = find_magic_index(my_array, 0, len(my_array))
print res

def find_magic_index_dups(array, start, end):
    if end <= start:
        return -1
    midpoint = (start + end) / 2
    if array[midpoint] == midpoint:
        return midpoint
    
    # search the left
    left_index = min(midpoint-1, array[midpoint])
    left = find_magic_index(array, start, left_index)
    if left >= 0:
        return left
    
    right_index = max(midpoint+1, array[midpoint])
    right = find_magic_index(array, right_index, end)
    return right

print find_magic_index_dups(my_array, 0, len(my_array))