# We can create empty functions by returning pass keyword

def hello_func():
    pass

# Empty function call returns None

# to call a function, we use parenthesis()
hello_func()

def hello_func1():
    print("Hello Function!")

hello_func1()

# fullform of DRY -> Dont't Repeat Yourself

# function is like a machine which upon calling, executed and returns a value
def hello_func2():
    return "Hello Function2."

print(hello_func2())

# as the function returning a string, we can use string method on it

print(hello_func2().upper())

# function takes parameters also we can assign a default parameter
def hello_function3(greeting):
    return f"{greeting} function"

print(hello_function3("Hello"))

def hello_function4(greeting, name = "You"): # here we are using a default value you, if no value mentioned for name it will take the default value
    return f"{greeting}, {name}"

print(hello_function4("welcome"))

# positional arguments using args, kwargs (It's an advace topic )

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ["Math", "Art"]
info = {"name": "John", "age": 22}

student_info(*courses, **info) # here we are unpacing the arguments value


