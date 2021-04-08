from collections import defaultdict
from collections import Counter
def top_three_letters(string):
    '''
    Given a string, find the top three most
    frequent letters
    This method should return a list
    of tuples, where the tuple contains
    the character and count
    >>> top_three_letters('abbccc')
    [('c',3),('b',2),('a',1)]
    >>> top_three_letters('aabbccd')
    [('a',2),('b',2), ('c',2)]
    '''

    # loop through the string and store the count
    # for each letter
    # sort the dictionary by the count and find the top
    # three most frequent letters
    # return a formatted list to match the output
    counter = defaultdict(int) # the default will be 0
    for c in string:
        counter[c] += 1
    top_three = sorted(counter, key=lambda k: counter[k], reverse=True)[:3]
    return [
        (letter, counter[letter])
        for letter in top_three
    ]


    # the Counter 
    # the counter class is a dict subclass
    # for counting hashable items 
    # we pass a hashable items and it will
    # count how many time each hash appears
    # and it will be stored in a dictionary
    return Counter(string).most_common(3)