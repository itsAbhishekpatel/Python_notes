class student:
    def detail(obj1,name = "Jao",age = 25): # we are passing the object itself and assign their values when it passing during calling the fucntion
        obj1.name = name
        obj1.age = age

obj1 = student() #creating an object by using the class 
obj1.detail("Abhishek",21)

print(obj1.name,obj1.age)
obj1.detail() # default values get assigned 
print(obj1.name,obj1.age)


        