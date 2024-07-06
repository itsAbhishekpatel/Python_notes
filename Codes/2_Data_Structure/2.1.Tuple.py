# tuples are immutable, it can't be change once created 
fruits = ("Apple","Mongo","Grapes")
print(fruits)

print(type(fruits))

# Unpacking of tuple 
a , *b = fruits

print(a,b) # sep each values

num_list = [1,2]
num0, num1 = num_list # you can also unpack the list 
print(num0,num1,type(num1))

# you can add two tuple 
updated_fruits = tuple(("Bananna",)) # always use , for declare single value tuple 
updated_fruits += fruits # concatinate tuples 

print(updated_fruits)

# using loop for access tuple 
for i in updated_fruits:
    print(i, end = " ")
print('\n____________')
for i in range(len(updated_fruits)):
    print(updated_fruits[i])


