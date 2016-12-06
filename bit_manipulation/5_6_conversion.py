# 5.6 Conversion
# ==============================================================================================
# Write a function to determine the number of bits you would need to flip to convert integer A
# to integer B.
# ==============================================================================================
def bits_to_convert(num1, num2):
    print "NUM1: {}, NUM2: {}".format(bin(num1), bin(num2))
    num_1s = num1 ^ num2
    print "NUM1s: {}".format(bin(num_1s))
    count = 0
    # now count how many 1s we have
    while num_1s != 0:
        if num_1s & 1 == 1: # we have a 1
            count += 1
        num_1s >>= 1
    return count

print bits_to_convert(45, 76)