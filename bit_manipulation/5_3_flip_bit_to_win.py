# 5.3 Flip Bit to Win
# ==============================================================================================
# You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to find the
# length of the longest sequence of 1s you could create.
# ==============================================================================================
def flip_bit(num):
    if ~a == 0: # all 1s, this is already the longest sequence
        return num.bit_length()
    cur_length = 0
    prev_length = 0
    max_length = 1
    while num != 0:
        if (a & 1) == 1: # current bit is a 1
            cur_length += 1
        elif (a & 1) == 0: # current bit is a 0
            if (a & 2) == 0: # check if next bit is 1
                prev_length = 0
            else:
                prev_length = cur_length
            cur_length = 0
        max_length = max(prev_length + cur_length + 1, max_length)
        a = a >> 1
    return max_length