# PyMathTools by John Elizarraras
# This is free and feel free to make any changes no need for credit but would appreciate it
from math import gcd

__all__ = ['binary_search', 'mod', 'to_ints', 'read_file', 'latex_gen_table']


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
        returns n mod modulus
    '''
    if not(float(modulus).is_integer()):
        raise ValueError('Modulus is not an integer')
    elif float(n).is_integer():
        return n % modulus
    else:
        if float(1/n).is_integer():
            if gcd(int(1/n), int(modulus)) != 1:
                raise ValueError('Inverse of n is not coprime with modulus')
            n = int(1/n)
            i = 1
            while (n * i) % modulus != 1:
                i = i + 1
            return i
        else:
            raise ValueError('Inverse of n is not an integer and n is a fraction')

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

def latex_gen_table(array, title, xaxis, yaxis, xmin, ymin, xmax, ymax):
    ''' generates a tikz graph with the provided points
    ----
    if there are too many points(out of memory) try using 'pdflatex --enable-write18 --extra-mem-bot=10000000 --synctex=1 <filename>' to make it compile
    ---

    Keyword arguments:
    array - A 2d array where the first column is the x value and the second is the y
    title(str) - the title of the graph. This will also be the title of the produced tex file
    xaxis(str) - the label for the x axis
    yaxis(str) - the label for the x axis
    xmin - the min x value on the x axis
    ymin - the min y value on the y axis
    xmax - the max x value on the x axis
    ymax - the max y value on y axis
    '''
    w = open(title + ".tex", "w+")
    w.write("\\documentclass{amsart}\n\\usepackage{pgfplots}\n\\begin{document}\n\\begin{tikzpicture}\n\\begin{axis}[\ntitle = {"+ title + "},\nxlabel={"+ xaxis +"},\nylabel={" + yaxis + "},\nxmin = " + str(xmin) + ", xmax=" + str(xmax) + ",\n")
    w.write("ymin=" + str(ymin) + ", ymax=" + str(ymax) + ",\nlegend pos=north west,\nymajorgrids=true,\ngrid style=dashed,\n]\n\n")
    w.write("\\addplot[\ncolor=blue,\nmark=square,\n]\ncoordinates {\n")
    for i in range(len(array)):
        w.write("(" + str(array[i][0]) + "," + str(array[i][1]) + ")")
    w.write("\n};\n\n")
    w.write("\end{axis}\n\end{tikzpicture}\n\end{document}")
