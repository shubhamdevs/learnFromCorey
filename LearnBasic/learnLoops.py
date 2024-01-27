nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

print("===========")
# break keyword break the loop and continue keyword continues the loop
    
for num in nums:
    if num == 3:
        print("Found!") # after printing this it breaks out of the loop 
        break
    print(num)

print("===========")

for num in nums:
    if num == 3:
        print("Found it!") # here it will not print the number 3, it will print Found it and moves on to print next number
        continue
    print(num)

# Nested Loop
    
for num in nums: # Here we are saying for every num of this list do this
    for letter in "abc": # here we are saying for every letter in abc of the num
        print(num, letter) # print the num and letter

for i in range(10): # it starts from 0 and goes till 9 (total 10 digits) and it doesn't include the last number
    print(i)

# if we want to start from 1, we pass in the value
    
for i in range(1, 11):
    print(i) # It will print 1 to 10

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1