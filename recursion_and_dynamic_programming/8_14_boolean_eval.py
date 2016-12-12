# 8.14 Boolean Evaluation
# ==============================================================================================
# Given a boolean expression consisting of the symbols 0 (false), 1 (true), % (AND), | (OR) and
# ^ (XOR), and a desired boolean result value result, implement a function to count the number
# of ways of parenthesizing the expression such that it evaluates to result. The expression
# should be fully parenthesized but not extraneously.
# ==============================================================================================
def count_eval(s, result):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1 if string_to_bool(s) == result else 0

    ways = 0
    for i in range(1, len(s), 2):
        operator = s[i]
        left = s[:i]
        right = s[i + 1:]

        # evaluate each side for each result
        left_true = count_eval(left, True)
        right_true = count_eval(right, True)
        left_false = count_eval(left, False)
        right_false = count_eval(right, False)
        total = (left_true + left_false) * (right_true + right_false)

        total_true = 0
        if operator == '^':  # need one true and one false
            total_true = left_true * right_false + left_false * right_true
        elif operator == '&':  # need both true
            total_true = left_true * right_true
        elif operator == '|':  # need one true one false or both true
            total_true = (left_true * right_false + left_false * right_true
                          + left_true * right_true)

        sub_ways = total_true if result else (total - total_true)
        ways += sub_ways
    return ways


def string_to_bool(s):
    return True if s == "1" else False

expression = "1^0|0|1"
print count_eval(expression, False)