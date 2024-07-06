student ={
    "name":"Abhishek",
    "age":18,
    "class":12

}

student.update({"section":"A"}) # update the dic 
print(student)
print(type(student))

print(student.keys()) # return list of all keys of dic 
print(student.values()) # retunr all values of dic 
print(student.items()) # return key value pair items of dic 

# student.pop("section")
# print(student)
# del student
# print(student) give an error becuase it get deleted
# student.clear() # list become empty 

# print(student) # an empty lsit is present 

for i in student:
    print(i,student[i]) # retunr key and their value 

family = {
    "child1" : { "name":"abhishek",
                "age": 12

    },

    "child2":{
        "name":"Kamlesh",
        "age":21
    }

}

print(family["child1"]["name"])




