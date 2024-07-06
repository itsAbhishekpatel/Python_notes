# number = input("Eneter the number:")
# print(number)

x, y = input("Enter the number:").split(",") # using split func

print(x,y)

# taking multiple values from users using map and split function 
x,y,z = map(int,input("Three number:").split())

# taking user input using list
x , y = [int (i) for i in input("Num: ").split()]
print(x,y)




