message = "Hello World!"

print(len(message))
print(message.lower())
print(message.upper())
print(message.count("l"))

print(message.find("Universe"))
# It will print -1, which means the it can't find the value and giving a falsy value

new_message = message.replace("World", "Universe")
# the fist parameter takes which world to replace
# and the second parameter takes by which thing we need to replace with
# this method returns a value which we have to store some place

print(new_message)


greeting = "Hello"
name = "Michael"

message = greeting + name
print(message)

# Here we are using formated string, first we decleare variable place holder and then with the help of format method 
# we mention the variables, all this enclosed in quation.
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)


print(f"{greeting}, {name.upper()}. Welcome!")


## this below three code will help in finding documentation
# print(dir(name))
# print(help(str))
# print(help(str.lower))



human = "anindita"
count = len(human)
print(type(human))
print(type(count))