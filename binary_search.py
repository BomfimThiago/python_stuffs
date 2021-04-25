# binary_iterative
# This method has a little problem
# if inside the list there are 2 or more elements
# we can not guarantee which element will be picked off
# by the method
def binary_iterative(arr, search_item):
    """Function to look in an array for 
    a specific item, if the item is found
    return the index of it.
    :params arr:List of the elements
    :params search_item: Element searched
    :return index of the element found
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        middle_index = (left + right) // 2
        middle_elem = arr[middle_index]

        if middle_elem == search_item:
            return middle_index
        elif middle_elem < search_item:
            left = middle_index + 1
        else:
            right = middle_index - 1 
    return None

# print(binary_iterative([1,2,3,4,5], 5))
# print(binary_iterative([3,4,4,5,5,7], 4))


def binary_leftmost(arr, search_item):
    """Function to look in an array for 
    a specific item, if the item is found
    return the index of it.
    Here we guarantee that, if there are
    2 or more elements equals to the looked for 
    element, than the method will bring the index
    of the left most elem.
    ex ...[1, 2, 3, 3,4]
    the method will always bring the index 2
    because it is the index o the left most element.

    :params arr:List of the elements
    :params search_item: Element searched
    :return index of the element found
    """
    left_most_index = binary_iterative(arr, search_item)

    if left_most_index is None:
        return None
    # To guarantee that we will not have a negative
    # index returned if we have a list where all elements are
    # equals to the looked for element,  
    # we have to apply another condition which
    # will evaluate de left_most_index only 
    # if it is equal or greater than 0
    while arr[left_most_index] == search_item and left_most_index >= 0:
        left_most_index -= 1

    # Tenho que adicionar esse 1 no final porque
    # quando ele saí do while ele já diminui um do 
    # index que deve ser retornado
    return left_most_index + 1

print(binary_iterative([3,4,5,5,9,9,10], 5))
print(binary_leftmost([3,4,5,5,9,9,10], 5))


def binary_recursive(elements, search_item, index_mod=0):
    """This function will bring the index of the search_item
    or None if not found
    The index_mod is a random number picked to increase the 
    speed of the alghoritm
    :params elements:List of the elements
    :params search_item: Element searched
    :params index_mod: random number which will be called in each call of the function
    :return index of the element found
    """
    while len(elements) > 0:
        middle_index = len(elements) // 2
        middle_elem = elements[middle_index]

        if middle_elem == search_item:
            return middle_index + index_mod
        elif middle_elem < search_item:
            return binary_recursive(
                elements[middle_index+1:],
                search_item,
                index_mod + middle_index + 1
            )
        else:
            return binary_recursive(
                elements[middle_index+1:],
                search_item,
                index_mod
            )
    return None


"""
Some things to get note

#Too long int to be divided, (library which use C or other
# language where the int type is limited)
middle_index = (left + rigth) // 2 is better writen like this:
middle_index = left + (right - left) // 2