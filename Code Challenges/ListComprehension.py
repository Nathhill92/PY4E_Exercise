# Challenges:
# Use a dictionary comprehension to count the length of each word in a sentence.
sentence = "This is a test sentence to help me learn list comprehension now this is a really long run on sentence that does not make any sense oh no."
newdict = {x:len(x) for x in sentence.split()}
print(newdict)

# Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
# Write the old fashioned way first to better understand task
# Create dictionary for later reporting
#newdict = {x: [] for x in range(2,10)}
# Old fashioned way
# for x in newdict:
#     for y in range(1,1000):
#         if y%x == 0:
#             newdict[x].append(y)

# # List comprehension way
# [y for y in newdict if [newdict[y].append(x) for x in range(1,1001) if x%y == 0]]

# # Print output
# for key, value in newdict.items():
#     print(key,value)

#better solution
results = {number:[x for x in range (1,1001) if x%number == 0] for number in range(2,10)}
#output
for key, value in results.items():
    print(key, value)


# For all the numbers 1-1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by
# newdict = {x: [] for x in range(1,1001)}
# [y for y in newdict if [newdict[y].append(x) for x in range(9,1,-1) if y%x == 0]]

# # Print output
# for key, value in newdict.items():
#     if value != []:
#         print(key,max(value))

#better solution
results = {number:max([x for x in range(1,10) if number % x == 0])for number in range(1,1001)}

#output
for key, value in results.items():
    if value > 1:
        print(key, value)

#Warm up
# Using a list comprehension, create a new list called "newlist" out of the list "numbers", which contains only the positive numbers from the list, as integers.
print("\n\n")
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(x) for x in numbers if x > 0]
print(newlist)

# Create a list of numbers divisible by 3, between 0-100
numbers = list(range(100))
newlist = [x for x in numbers if (x % 3 == 0)]
print(newlist)

# Find all of the numbers from 1-1000 that are divisible by 7
numbers = list(range(1, 1000))
newlist = [x for x in numbers if (x % 7 == 0)]
print(newlist)
# Find all of the numbers from 1-1000 that have a 3 in them
numbers = list(range(1, 1000))
newlist = [x for x in numbers if ("3" in str(x))]
print(newlist)
# Count the number of spaces in a string
sentence = "This is a test sentence to help me learn list comprehension."
newlist = [x for x in sentence if x == " "]
print(len(newlist),"spaces in sentence.")
# Remove all of the vowels in a string
sentence = "This is a test sentence to help me learn list comprehension."
newlist = [x for x in sentence if x.lower() not in ["a", "e", "i", "o", "u"] ]
print(''.join(newlist))
# Remove all of the consonants in a string
sentence = "This is a test sentence to help me learn list comprehension."
newlist = [x for x in sentence if x.lower() in ["a", "e", "i", "o", "u"] ]
print(''.join(newlist))
# Find all of the words in a string that are less than 4 letters
sentence = "This is a test sentence to help me learn list comprehension."
newlist = [x for x in sentence.split() if len(x) < 4]
print(newlist)

