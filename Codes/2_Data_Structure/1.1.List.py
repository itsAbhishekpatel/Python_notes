mylist = [1,2,3,4,5]
myname = ["Abhishek", "Rohan"]
mymix = ['Jay', 23, True ]

print(type(mylist)) # type is list it not become interger just becuse you assign int values 
print(type(mylist[0])) # but element is integer 

print(mylist[::-1]) # reverse the list using negative indexing 

print(mylist[1:4]) # last index will not including

print(mylist[0::2]) # goes in the end of the list and it take 2 steps 

# printting list using for loop 
for i in mylist:
    print(i, end = " ")

# check if item is in the list or not 
if "Abhishek" in myname:
    print("\nTrue")

else:
    print("There is no student of name Abhishek.")

blanklist = list() # or blanklist = []
print(blanklist)

mylist [2] = 100 # replace the 3rd vlaue of of the list
print(mylist)

# using insert() function 
myname.insert(1,"Kallu") # adding a new value at index 1 and new values are shifted
print(myname)
