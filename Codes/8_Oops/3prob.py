class school:
    name = "sarvodya"

obj = school()
obj.name = "Sarvodya Bal Vidyalaya" # overwrite the class attribute by assigning object attribute but its wrong
# here instance attribute is set 

print(obj.name) # print the instance attribute becuse its present and 
print(school.name) # it does not change! 