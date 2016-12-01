# 5.1 Insertion
# ==============================================================================================
# You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to
# insert M into N such that M starts at bit j and ends at bit i. You can assume that the bits j
# through i have enough space to git all of M. That is, if M = 10011, you can assum that there
# are at least 5 bits between j and i. You would not, for example, have j=3 and i=2, because M 
# could notfully bit between bit 3 and bit 2.
# ==============================================================================================
def insert(num1, num2, i, j):
    left_bitmask = ~ ((1 << j+1) - 1)
    right_bitmask = (1 << i) - 1
    bitmask = left_bitmask | right_bitmask
    num1 &= bitmask # cleared the middle bits
    insert_num = num2 << i
    return num1 | insert_num

print bin(180)
print bin(23)
res = insert(180, 23, 2, 6)
print res
print bin(res)

