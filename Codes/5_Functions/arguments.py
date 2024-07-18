# Here a function is define with one parameter value 
def greet(name,age):
    print(f"Hello, how are you {name}.")
    print(f"So you are {age}, years old.")


# Calling the greet function with, and passing an argumnent 

# greet("abhishek") # its is an postional argument, give an error we have to pass two arguments

greet("abhishek",21)
greet(21,"abhishek") # it does not make any sense

# keyword argument
# Keyword-only arguments mean whenever we pass the arguments(or value) by their parameter names at the time of calling the function in Python in which if you change the position of arguments then there will be no change in the output.

greet(name = "abhishek",age = 34)

