# 8.1 Triple Step
# ==============================================================================================
# A child running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at
# a time. Implement a method to count how many possible ways the child can run up the stairs.
# ==============================================================================================
def steps(denominations, cur_solution, remainder, solutions):
    if remainder == 0:
        solutions.append(cur_solution)
        return
    for denom in denominations:
        if remainder - denom >= 0:
            cur_solution.append(denom)
            steps(denominations, cur_solution[:], remainder-denom, solutions)
            cur_solution.pop()

def get_list_of_steps(denominations, num_steps):
    solutions = []
    steps(denominations, [], num_steps, solutions)
    return solutions

solutions = get_list_of_steps([1,2,3], 4)
print solutions

def count_steps_helper(n):
    memo = [-1] * (n+1)
    return count_steps(n, memo)
    
def count_steps(n, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if memo[n] > -1:
        return memo[n]
    else:
        memo[n] = count_steps(n-1, memo) + count_steps(n-2, memo) + count_steps(n-3, memo)
        return memo[n]

print count_steps_helper(4)