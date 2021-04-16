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
def bubble_sort(items):
    for i in range(len(items)):
        already_sorted = True
        # len(items) - i são os elementos que ainda faltam serem verificados
        # -1 porque eu não fazer a permuta do último elemento
        for j in range(len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                already_sorted = False
        if already_sorted:
            break
    return items

items = [random.randint(1, 1000) for _ in range(1000)]
print(bubble_sort(items)[1])
