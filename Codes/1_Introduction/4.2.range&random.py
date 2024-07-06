# defining a range using range function
# range(start, stop, step)
# Built  in funtion
x = range(6)
print(x)

for i in x:
    print(i,end=" ")
print("")

# define range function with it parameters 
y = range(2,10,2)
for i in y:
    print(i, end = " ")


# importing random module and use rand method to generate random value 
import random
ran_value = random.randrange(1,10)

# randrange is a method define in random module 
print("\n",ran_value)



