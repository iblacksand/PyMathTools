
def binary_search(array, target):
    """ Does a binary search on to find the index of an element in an array
        Keyword arguments:
        array - the array that contains the target
        target - the target element for which its index will be returned
        returns the index of target in array
    """
    lower = 0
    upper = len(array)
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # this two are the actual lines
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x

def mod(n, modulus):
    ''' A safer mod funtion instead of %, where fractions are acurately calculated
        Keyword arguments:
        n - the number to take modulo by
        modulus - the modulus
        returns n modo modulus
    '''
    if not(float(modulus).is_integer()):
        raise ValueError('Modulus is not an integer')
    elif float(n).is_integer():
        return n % modulus
    else:
        if float(1/n).is_integer():
            n = int(1/n)
            i = 1
            while (n * i) % modulus != 1:
                i = i + 1
            return i
        else:
            raise ValueError('Inverse of n is not an integer')
