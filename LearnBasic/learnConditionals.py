if True:
    print("Conditinal was True")

# Equality check
    
language = "Python"

if language == "Python": # It checks if the condition is true then it runs
    print("Conditional here is True")

if language == "Java":
    print("Language is Java")
elif language == "Python":
    print("Language is Java")
else:
    print("no match") # it will go this block if no condition meet true

# and
# or
# not 
    
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # It will return true, because it checks value

print( a is b) # It will return false, because it checks for the id and two different variable has different ids

# id function gives us the id of a variable
print(id(a))
print(id(b)) 

c = a  # if we copy a variable to another variable then it's id will be same
print(id(c))

# falsy & turly value

# false, none, zero (0), empyth sequence(empty list, emply dict, empty tuple, empty set) this all return a false

# any number greater than 0 will return true, string will a single charcter will give true



