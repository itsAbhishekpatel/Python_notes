# List , tuples , string 
# range 

city = "Delhi"
print(city,type(city))

#indexing
# city[start:stop:steps] 

print(city[1])

# string slicing 
print(city[1::2])

print(city[::-1]) # reverse

print(len(city))

for letter in city:
    print(letter,end=" ")

for letter in range(len(city)):
    print(city[letter])

