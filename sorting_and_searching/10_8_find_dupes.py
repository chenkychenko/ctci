# 10.8 Find Duplicates
# ==============================================================================================
# You have an array with all the numbers from 1 to N, where N is at most 32,000. The array may
# have duplicate entries and you do not know what N is. With only 4KB of memory available, how
# would you print all duplicate elements in the array?
# ==============================================================================================
def print_dupes(array):
    # first create bitvector
    bit_vector = [0] * 32000/32 # initialize as array of ints
    for i in range(len(array)):
        mark_bit(bit_vector, array[i])

def mark_bit(bit_vector, val):
    i = val / 32 # get which integer we need to toggle bits for
    b = val % 32 # get which bit we need to toggle
    int_to_use = bit_vector[i]
    bit_mask = 1 << b # shift left b times
    if int_to_use & bit_mask > 0: # means there was a 1 there!
        print val # print the dupe integer
    else:
        bit_vector[i] = int_to_use | bit_mask