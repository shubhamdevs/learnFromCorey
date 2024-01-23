# Arithmatic Operator
# Floor Division: /
# Exponent: **
# Modulus: %

print( 3 // 2)

print(3 % 2)

print("******************************")

# abs method gives us only the absolute value
print(abs(-3))
print(abs(3.678))

# round method round off the number to it's nearest integer
# round method also takes a second parameter as integer, 
# that defines how many digit from the decimel point we have to round off
print(round(3.75))
print(round(3.8667, 1))

# Comparision Operator
# == Equal to 
# != Not Equal to

print("******************************")

# Type Casting
# we have to wrap the given data type with the intendent data type while type casting

num_1 = "100"
num_2 = "200"

print(num_1 + num_2)
# when we add two strings it adds the value side by side and it is called string concatination.

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)