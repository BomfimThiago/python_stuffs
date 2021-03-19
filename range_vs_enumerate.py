def fizz_buzz(numbers):
    """
    given a list of integers:
    1. Replace all integers that are evenly divisible by 3
    with 'fizz'
    2. Replace all integers divisible by 5 with 'buzz'
    3. Replace all integers divisible by both 3 and 5 with
    'fizzbuzz'
    >>> numbers = [45, 22, 14, 65, 97, 72]
    >>> fizz_buzz(numbers)
    >>> numbers
    ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
    """

    # solution using range
    for i in range(len(numbers)):
        num = numbers[i]
        if num % 3 == 0:
            numbers[i] = 'fizz'
        if num % 5 == 0:
            numbers[i] = 'buzz'
        if num % 3 == 0 and num % 5 == 0:
            numbers[i] = 'fizzbuzz'

    # solution using enumerate
    # Enumerates iterate over an iterable and returns an list of tuple where the first 
    # element is the index and the second is the value
    for i, num in enumerate(numbers):
        if num % 3 == 0:
            numbers[i] = 'fizz'
        if num % 5 == 0:
            numbers[i] = 'buzz'
        if num % 3 == 0 and num % 5 == 0:
            numbers[i] = 'fizzbuzz'
