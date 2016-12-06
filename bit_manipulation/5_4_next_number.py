# 5.4 Next Number
# ==============================================================================================
# Given a positive integer, print the next smallest and the next largest number that have the
# same number of 1 bits in their binary representation.
# ==============================================================================================
def next_num(num):
    # first we count the 0s and 1s from the right
    c = num
    c0 = 0
    c1 = 0
    print "NUM IS {}".format(bin(c))
    while (c & 1) == 0 and c != 0: # count c0s
        c0 += 1
        print "adding 1 to c0"
        c = c >> 1
    
    while (c & 1) == 1: # count c1s
        c1 += 1
        c >>= 1
    print "There are {} trailing 0s and {} 1s in this num".format(c0, c1)
    # set the non-trailing zero to 1
    p_bitmask = 1 << (c1+c0)
    print "set non-trailing zero to 1 mask: {}".format(bin(p_bitmask))
    num |= p_bitmask
    print "AFTER setting 0 to 1: {}".format(bin(num))
    # clear all bits to right of p
    clear_mask = ~(p_bitmask-1)
    print "CLEAR MASK: {}".format(bin(clear_mask))
    num &= clear_mask
    print "NUM NOW: {}".format(bin(num))
    # add back the (c1-1) 1s all the way to the right
    add_1s_mask = (1 << c1-1) - 1
    return num | add_1s_mask

print  "BINARY NEXT NUM===="
# print bin(54)
print bin(next_num(45))

def prev_num(num):
    c = num
    c0 = 0
    c1 = 0
    while c & 1 == 1:
        c1 += 1
        c >>= 1
    while c & 1 == 0 and c != 0:
        c0 += 1
        c >>= 1
    # clear all bit including p onwards
    p = c1 + c0
    clear_mask = (~0) << (p + 1)
    num &= clear_mask
    print "NUM AFTER CLEARING P=> BITS: {}".format(bin(num))
    # add back the c1+1 1s, to the leftmost side
    add_1s_mask = (1 << (c1+1)) -1
    print "ADD 1S MASK: {}".format(bin(add_1s_mask))
    add_1s_mask <<= (c0-1)
    return num | add_1s_mask

print "BINARY PREV NUM!"
print bin(prev_num(45))