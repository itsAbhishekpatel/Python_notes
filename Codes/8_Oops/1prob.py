class programmer:
    # make a class attribute 
    company = "Micosoft"
    def __init__(self,name,salary,age) -> None:
        print()
        self.name = name
        self.salary = salary
        self.age = age


obj1 = programmer("Abhisek","12,00,000","26")

print(obj1.company,obj1.name,obj1.salary,obj1.age)
        