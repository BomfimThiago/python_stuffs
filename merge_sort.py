import random
import time

def merge_sorted_list(left, right):
    left_index, right_index = 0, 0
    return_list = []
    while (len(return_list) < len(left) + len(right)):
        left_item = left[left_index] if left_index < len(left) else float('inf')
        right_item = right[right_index] if right_index < len(right) else float('inf')

        if left_item < right_item:
            return_list.append(left_item)
            left_index += 1
        else:
            return_list.append(right_item)
            right_index += 1
    return return_list

def merge_sort(items):
    if (len(items) <= 1):
        return items

    midpoint = len(items) // 2
    left, right = items[:midpoint], items[midpoint:]
    return merge_sorted_list(
        merge_sort(left),
        merge_sort(right)
    )
