from PyMathTools import *
# binary_search
a = [6,7,8,9,10]
print(binary_search(a, 8)) # returns 2

# mod
print('34 mod 7 = ' + str(mod(34,7))) # returns 6
print('1/4 mod 7 = ' + str(mod(1/4,7))) # returns 2
# print('4 mod 5.5  = ' + str(PyMathTools().mod(4, 5.5))) - this would throw an exception
print(read_file("nums.txt"))
