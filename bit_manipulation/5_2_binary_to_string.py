# 5.2 Binary to String
# ==============================================================================================
# Given a real number between 0 and 1 (like 0.72) that is passed in as a double, print the binary
# representation. If the number cannot be represented accurately in binary with at most 32
# characters, print "ERROR."
# ==============================================================================================
def print_binary(num):
    if num >= 1 or num <= 0:
        return "ERROR"
        
    binary = []
    binary.append('.')
    while num > 0:
        if len(binary) >= 32:
            return "ERROR"
        r = num * 2
        if r >= 1:
            binary.append('1')
            num = r-1
        else:
            binary.append('0')
            num = r
    return ''.join(binary)

print print_binary(0.75)