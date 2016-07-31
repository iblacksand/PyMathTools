# PyMathTools by John Elizarraras
# This is free and feel free to make any changes no need for credit but would appreciate it


__all__ = ['binary_search', 'mod', 'to_ints', 'read_file']


def binary_search(array, target):
    """ Does a binary search on to find the index of an element in an array. WARNING - ARRAY HAS TO BE SORTED
        Keyword arguments:
        array - the array that contains the target
        target - the target element for which its index will be returned
        returns the index of target in array
    """
    lower = 0
    upper = len(array)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:
                break
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

def to_ints(array):
    ''' converts everything in an array into ints

    Keyword arguments
    array - the array containing the ints
    returns an array with the conveted ints
    '''
    for i in range(len(array)):
        array[i] = int(array[i])
    return array

def read_file(f):
    ''' reads a file and converts the file into an array of floats. It seperates numbers by spaces and will go through all the lines. You can use the to_ints function to convert it.

    Keyword arguments:
    f - the path/name of the file

    returns an array of floats
    '''
    r = open(f, "r")
    s = str(r.readline())
    a = []
    while s != "":
        s = s.strip().split(" ")
        for i in s:
            a.append(float(i))
        s = str(r.readline())
    return a
