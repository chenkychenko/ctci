# 8.11 Coins
# ==============================================================================================
# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
# pennies (1 cent), write code to calculate the number of ways of representing n cents.
# ==============================================================================================
def make_change(amount, denoms, index):
    if index >= len(denoms)-1:
        return 1 # base case
    coin = denoms[index]
    ways = 0
    for i in range((amount / coin)+1):
        rem_amount = amount - i*coin
        ways += make_change(rem_amount, denoms, index+1)
    return ways

denoms = [25,10,5,1]
res = make_change(2, denoms, 0)
print res