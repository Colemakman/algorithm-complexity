import timeit
import importlib
import random


<<<<<<< HEAD
# Basically higher number = higher degree of accuracy but tests take longer.
NUMBER = 3 

# The names of the .py files you want to test (without the .py"
files = ["sub_sequence_sum_inefficient", "sub_sequence_sum_efficient"]
=======
# The names of the .py files you want to test (without the .py)
files = ["shuffle", "sort"]
>>>>>>> 106b83df730b3f9aca38ba31cc8b4b58d1eea52b

# The input sizes you want to test
inputs = list(range(5000, 100001, 5000))

def time_algorithm(algorithm, size):
    setup = f'from {algorithm} import {algorithm};'

    test_input = list(range(1, size+1))
    random.shuffle(test_input)
    test = f'{algorithm}({test_input})'
    
    time_taken = timeit.timeit(test, setup=setup, number=NUMBER)
    return time_taken / NUMBER

for alg in files:
    for size in inputs:
        print(f'Algorithm: {alg}, Input size: {size}, Time: {time_algorithm(alg, size)}')
    print("-------")
