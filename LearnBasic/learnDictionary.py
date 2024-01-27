# Dictionary 
# It stores data in key-value pair. Where key is a uniqui identifier and it holds the value

student = { 
    "name": "Shubham",
    "age": 24,
    "courses": ["Math", "CompSci"] # Value can be any data type(list, tuples or sets) and keys are seperated by comma
           }
print(student)
print(type(student))

print(student["name"])

# if the key isn't present in the dictionary it will give us "KeyError". To Prevent this we have to use get method

print(student.get("phone")) # It will return none
print(student.get("phone", "Not Found")) # if we give a second parameter, it will print the second parameter if the key isn't present in the dictonary.

student["phone"] = "555-5555" # it will add a new key to the dictionary student

student["name"] = "Anindita" # if the key is already present in the dictionary, it will update the value of that key

print(student)

# update method helps in adding or updating many key all at once in a dictionary
student.update({"age": 22, "phone": "555-4444", "experience": 2}) # here it will add a new key pair(experience: 2) in the dictionary

print(student)

del student["age"] # del keyword hlep in deleting a key in a dictionary

experience = student.pop("experience") # pop method not only removes the key but also return the value which we can assign in a variable

print(experience)
print(student)

# to know how many keys a dictionary has we use len method

print(len(student))

print(student.keys()) # keys method returns all the keys

print(student.values()) # values method returns all the values of a dictionary

print(student.items()) # items method returns all the key value pair

# working with for loop

for key in student: # here we are only accessing the keys 
    print(key)

for key, value in student.items(): # to iterate over key and value we have to use items method in a for loop
    print(key, value)