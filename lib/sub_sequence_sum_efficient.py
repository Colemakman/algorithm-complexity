# sub-sequence sum, given array L and value K, find a subarray of L that sums to K. Return true if this is possible, and false othewise.

# Efficient second method: Time complexity O(n)

import random


default = random.randint(1, 100)

def sub_sequence_sum_efficient(array, k=default):

    n = len(array)

    subset = ([[False for i in range(k + 1)] for i in range(n+1)])

    for i in range(n+1):
        subset[i][0] = True 

    for i in range(1, k+1):
        subset[0][i] = False

    for i in range(1, n+1):
        for j in range(1, k+1):
            if j < array[i-1]:
                subset[i][j] = subset[i-1][j]
            if j >= array[i-1]:
                subset[i][j] = (subset[i-1][j] or subset[i-1][j-array[i-1]])

    return subset[n][k]
