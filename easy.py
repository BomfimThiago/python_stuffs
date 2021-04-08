def majority_element_indexes(lst):
    '''
    Return a list of indexes of the majority
    element.
    Majority element is the element that appears
    more than floor(n/2)times.
    If there is no majority element, return []
    >>> majority_element_indexes([1,1,2])
    [0,1]
    >>> majority_element_indexes([1,2])
    []
    >>> majority_element_indexes([])
    []
    '''
    # Sempre que pensar em frequencia de letras, ou algo
    # pensar em collections.Counter
    from collections import Counter
    if lst == []:
        return []

    counter = Counter(lst)
    top_elems = sorted(
        counter.keys(),
        key=lambda x: -counter[x]
    )
    top_count = max(counter.values())
    maj_elem = [
        elem for elem, count
        in counter.items if count == top_count
    ][0]
    print(top_count)
    if counter[maj_elem] > len(lst) // 2:
        return [
            i for i, elem in enumerate(lst)
            if elem == maj_elem
        ]
    else:
        return []
    print(top_elems)
