# 10.1 Sorted Merge
# ==============================================================================================
# You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold
# B. Write a method to merge B into A.
# ==============================================================================================
def merge(longer, shorter):
    if longer and shorter:
        # find last element in A
        i = len(longer)-len(shorter)-1
        j = len(shorter)-1
        cur = len(longer)-1
        while i >= 0 and j >= 0:
            if longer[i] > shorter[j]: # longer element should be copied into end
                longer[cur] = longer[i]
                i -= 1
            else:
                longer[cur] = shorter[j]
                j -= 1
            cur -= 1
        if i >= 0: # copy all elements from longer into right indices
            longer[cur] = longer[i]
            i -= 1
            cur -= 1
        if j >= 0: # copy all elements from shorter into right indices
            longer[cur] = shorter[j]
            j -= 1
            cur -= 1
    return longer

a = [1,4,6,7,0,0,0,0]
b = [2,3,5,9]
merge(a, b)
print a