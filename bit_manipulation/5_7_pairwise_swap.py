# 5.7 Pairwise Swap
# ==============================================================================================
# Write a program to swap off and even bits in an integer with as few instructions as possible,
# (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).
# ==============================================================================================
def pairwise_swap(num):
    odd_mask = 0xaaaaaaaa
    odd_bits = num & odd_mask
    odd_bits >>= 1
    even_mask = 0x55555555
    even_bits = num & even_mask
    even_bits <<= 1
    return odd_bits | even_bits

print bin(pairwise_swap(45))