# sub-sequence sum, given array L and value K, find a subarray of L that sums to K. Return true if this is possible, and false othewise.

# Inefficient first method: Time complexity O(n^3)

import random

default = random.randint(0, 100)

def sub_sequence_sum_inefficient(array, k=default):
    length = len(array)

    if k == 0:
        return True

    for i in range(length):
        for j in range(i+1, length+1):
            subarr = array[i:j]
            if sum(subarr) == k:
                return True
    return False


