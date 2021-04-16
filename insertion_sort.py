import time
import random

def timed_func(func_to_time):
    def timed(*args, **kwargs):
        start = time.perf_counter()
        res = func_to_time(*args, **kwargs)
        print(time.perf_counter() - start)
        return res
    return timed

@timed_func
def insertion_sort(items):
    for i in range(1, len(items)):
        current_item = items[i]
        j = i - 1 # first element of the list, we start from the second

        while(j >= 0 and current_item < items[j]): # Break when the current el is in the right place
            items[j + 1] = items[j] # Moving this item up
            j -= 1

        items[j + 1] = current_item
    return items

items = [random.randint(1, 1000) for _ in range(1000)]
print(insertion_sort(items)[1])