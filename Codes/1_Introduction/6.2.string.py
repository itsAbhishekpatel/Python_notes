
# METHODS IN STRINGS 
sentence = "here you are"

print(sentence.title()) # string method do not change the original value, they return a new value
print(sentence.upper())

print(sentence) # original value does not change

str_Hello = " Hello, World "
print(str_Hello.split(",")) # split function return values in list
print(str_Hello.strip()) # strip function which remove space from begninng and end of the string 

# a = sentence.join()
# print(a)

list_ = ["A","B","C"]

joinele = "-".join(list_) # join elements of list using join function where we pass iterable and join them into a string 

print(joinele)

