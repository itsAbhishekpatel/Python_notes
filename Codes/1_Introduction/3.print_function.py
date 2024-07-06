print("This is a string")

# Parameters in string 
# print(object(s), sep=separator, end=end, file=file, flush=flush)

Day = 10
Month = "June"
Year = 2024
print(Day,Month,Year)
print(Day,Month,Year,sep="-") # using seperate parameter
print(Day,Month,Year,sep="-",end="*") # using end parameter

# formating of string 
name = "Abhishek"
age = 24
print(f"Name {name} and age {age}") # by default end is new line but you overwrite with * that is why it is printing in the same lie


