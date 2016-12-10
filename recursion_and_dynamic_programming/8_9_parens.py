# 8.9 Parens
# ==============================================================================================
# Implement an algorithm to print all valid (ie, properly opened and closed) combinations of n
# pairs of parentheses.
# ==============================================================================================
def add_parens(left_rem, right_rem, chars, results):
    if left_rem < 0 or right_rem < left_rem:
        return  # invalid state
    if left_rem == 0 and right_rem == 0:
        results.append(''.join(chars))
    else:
        chars.append('(')
        add_parens(left_rem - 1, right_rem, chars, results)
        chars.pop()

        chars.append(')')
        add_parens(left_rem, right_rem - 1, chars, results)
        chars.pop()


def generate_parens(count):
    chars = []
    results = []
    add_parens(count, count, chars, results)
    return results


res = generate_parens(4)
print res