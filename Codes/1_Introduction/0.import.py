# Importing timr module/ package 
import time

# The code uses the time module to retrieve the current time in seconds since the Unix epoch (January 1, 1970).
cur = time.time()

# Current time 
curr = time.ctime(cur)
print("Current time:", curr)

# Import in Python is similar to #include header_file in C/C++
import math
pie = math.pi
print("The value of pi is : ", pie)

# Importing Module using “from”
# In the above code module, math is imported, and its variables can be accessed by considering it to be a class and pi as its object. The value of pi is returned by __import__(). pi as a whole can be imported into our initial code, rather than importing the whole module. We can also import a file in Python using from.

from math import pi
print(pi)

# Import Python Built-In Modules
import random
 
# Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print("Random Number:", random_number)

# Import a Module and Assign an Alias in Python
# Import the 'math' module with the alias 'm'
import math as m
 
# Use functions from the 'math' module with the alias
result = m.sqrt(25)
print("Square root of 25:", result)

# Importing `*` in Python
# In the above code module, math is not imported, rather just pi has been imported as a variable. 
# All the functions and constants can be imported using *. 

from math import *
print(pi)
print(factorial(6))


