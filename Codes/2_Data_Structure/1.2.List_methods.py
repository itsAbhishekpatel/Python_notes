# Methods is lists 

name = ["abhishek","mohan","ram"]
surname = ["patel","verma","singh"]

name.extend(surname) # extend the original name list
print(name)

name.pop() # removing last elements from the list, you can also specify the index
print(name)

name.append("End of the string") # adding a value in the end of the list
print(name)

[print(x) for x in name ] # short hand 

# iterate list using while loop 
print("---------print list value using while loop---------")
i = 0
while i < len(name):
    print(name[i])
    i +=1

# list comprehension 
num = [ i for i in range(1,10)]
print(num)

num = [ i for i in range(1,10) if i%2 == 0] # you can use condition also
print(num)

surname.sort() # sorting the original list 
print(surname)

number = [ i for i in range(11)]
number.sort( reverse = True)

print(number)

new_name = name.copy() # copying the list in new list
print(new_name)