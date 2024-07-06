class calulator:
    # you can also assign object value by usning construtor 
    # istead of assigning every time
    # we are not using self here so we make it static method, not want to add instance attribute  
    @staticmethod
    def greet():
        print("Here you can find Square, Cube and root of any number!")
    
    def __init__(self,num) -> None:
        self.num = num
    # square function
    def square(self,num:int) -> None:
        self.num = num
        # return self.num**2
        print(f"Square of {self.num} is {self.num**2}")

    def cube(self,num) -> None:
        self.num = num
        print(f"Cube of {self.num} is {self.num**3}")
    
    def sqroot(self,num):
        self.num = num
        print(f"Square root of {self.num} is {self.num**0.5}")
# In the following code: def f(x) -> int: return int(x) the -> int just tells that f() returns an integer 
# (but it doesn't force the function to return an integer).

obj1 = calulator(10)
obj1.greet()
obj1.square(5)
obj1.cube(10)
obj1.sqroot(25)

# explain what function is going to return 
print(obj1.square.__annotations__) 

