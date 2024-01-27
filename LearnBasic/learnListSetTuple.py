courses = ["History", "Math", "Physics", "CompSci"]

print(courses)
print(len(courses))
print(courses[0])

# Here we are using negetive(-ve) indexing it stats form -1 which is last item of the list
print(courses[-2])

# Here first index is inclusive but the second index is exclusive
# if we give missing index then it will be go till end of the list
print(courses[0:2])
print(courses[2:])

# Here we are using append method which adds a new item to the end of the list
courses.append("Art")
print(courses)

# the insert method takes two argument, first one is for the insertion position and second one is the item in a list
courses.insert(0, "Cosmiology")
print(courses)

# the extend method adds items of a list to the main list and it takes  list as argument
courses_2 = ["Psycology", "Biology"]
courses.extend(courses_2)
print(courses)

# Removing items form a list
courses.remove("Math") # remove method takes a item to remove
popped = courses.pop() # it's removes the last item of a list and return the last item so we can assign it in a variable

# Sorting in list

courses.reverse() # reverse method reverses the items in a list
print(courses)

courses.sort() # sort method sorts item's in alphabetical order for string and numerical order for int, float
print(courses)

numlist = [ 30, 2, 59, 10]
numlist.sort()
print(numlist)

numlist.sort(reverse= True) # if we pass reverse parameter it will print the list item in ascending order
print(numlist)

sorted_courses = sorted(courses) # sorted function doesn't modify the main list, it returns a modified list which we can declear in a variable
print(sorted_courses)

# min, max, sum functions for list
print(min(numlist))
print(max(numlist))
print(sum(numlist))

# finding a value in a list

new_course = ["History", "Math", "Physics", "CompSci"]

# to find an index of a item in a list we use index method and it takes a item as a parameter

print(new_course.index("Math")) # ⚠️ If we try to get index of unlisted item, we will get value error

print("Art" in new_course) # if we want to check if something is present in our list we use in 


# We can use for loop to print items of a list with in function, this will loop through each item here sub(we can give any name)
# in the list
for sub in new_course:
    print(sub)

# we can use enumerate function to give an index to the items we have to pass index and item while using for loop
# enumerate function takes the list and the index start from 0 index. if we want to start with a different index we pass start parameter
for index, sub in enumerate(new_course, start = 1):
    print(index, sub)

# the join method converts a list in a single string. It takes two things, in quatation by which we will seperate it and the list as a parameter
course_str = ",".join(new_course)
print(course_str)
print(type(course_str))

# the split method converts a single string in a list. It takes a parameter by which we need to make item of a new list
new_list = course_str.split(",")
print(new_list)
print(type(new_list))

# tuples are same as list but it's immutable that means after assigning we can't change it value can't 
# change it's value or modify or reassign it's value

tuple_1 = ("History", "Math", "Pysics", "CompSci")
print(type(tuple_1))

# Sets are same like list and tuples but it doesn't care about order and it removes duplicate values
cs_courses = {"History", "Math", "Physics", "CompSci", "Math"}
print(cs_courses) # it will print -> {'Physics', 'Math', 'History', 'CompSci'} # Here Math has mentioned only one time

# set's are very optimized and runs very fast
print("Math" in cs_courses)

# we can do set operations in sets

art_courses = {"History", "Math", "Art", "Design"}

print(cs_courses.intersection(art_courses)) # the intersection method here take a set as parameter and gives intersecting items
print(cs_courses.difference(art_courses)) # the difference method prints the differences
print(cs_courses.union(art_courses)) # the union method prints all the items in both sets
# print(dir(cs_courses))

# Empty Decleations
# Empty Lists
empty_list = []
empty_list = list()

# Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Empty set
empty_set = {} # This isn't right! It's a dict
empty_set = set() # This is the right way to declear an emplty set
