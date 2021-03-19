"""
Generators is still a way to iterate over a sequence
with the benefits that it is lazy loaded
"""
g = (i for i in range(6))
print(g)

# a generator object takes less memory space than a list object
import sys
lst = [i for i in range(1, 1001)]
sys.getsizeof(lst) #9032
g = (i for i in range(1, 1001))
sys.getsizeof(g) #128