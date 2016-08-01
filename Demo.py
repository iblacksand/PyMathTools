# import statement
from PyMathTools import *
# * will import all of the functions

# binary_search
a = [6,7,8,9,10]
print(binary_search(a, 8)) # returns 2

# mod
print('34 mod 7 = ' + str(mod(34,7))) # returns 6
print('1/4 mod 7 = ' + str(mod(1/4,7))) # returns 2
# print('4 mod 5.5  = ' + str(PyMathTools().mod(4, 5.5))) - this would throw an exception

# read_file
a = read_file("nums.txt")
print(a)

# to_ints
a = to_ints(a)
print(a)

# latex_gen_graph
b = [[0,0], [1,1], [2,2], [4,4], [5,5]]
latex_gen_graph(b, "Line of the form $y = x$", "$x$", "$y$", 0, 0, 5, 5)

# is_prime
print(is_prime(99)) # returns false
print(is_prime(101)) # returns true
