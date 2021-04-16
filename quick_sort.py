import random
def quicksort(items):
    if(len(items) <= 1):
        return items

    pivot = random.choice(items)
    less_than_pivot = [x for x in items if x < pivot]
    equal_to_pivot = [x for x in items if x == pivot]
    greater_than_pivot = [x for x in items if x > pivot]
    return quicksort(less_than_pivot) + equal_to_pivot + quicksort(greater_than_pivot)