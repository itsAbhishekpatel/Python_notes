even_number = {2,4,6,8}

print(even_number) # sets are unorder and can change the values 
print(type(even_number))

# even_number[0] = 5  can't change the values 
# but you can add values 
even_number.add(10) # only take one argument at a time 
print(even_number)

# using loop to acess values 
for i in even_number:
    print(i)

# i = 0
# while i<len(even_number):
#     print(even_number[i], end=" ")
#     i+=1
# print(even_number[0])  can run the code, you cannot acess set items by key or index value 

even_number.remove(2)
print(even_number)






