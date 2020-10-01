# Exercise 1: Write a while loop that starts at the last character in 
# the string and works its way backwards to the first character in the string, 
# printing each letter on a separate line, except backwards.

testStr = "test and stuff"
i=0

while i <= len(testStr):
    print(testStr[-i])
    i+=1

# Exercise 2: Given that fruit is a string, what does fruit[:] mean?
# it will print the entire string for fruit

fruit = "apple, banana, kiwi"
print(fruit[:])

#Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

def LetterCount(userLetter, testStr):
    count=0
    for letter in testStr:
        if letter == userLetter:
            count += 1
    return count

userLetter = input("\nWhat letter would you like to check for: ")
print("We found", LetterCount(userLetter, testStr), "instance(s) of your letter.\n")

#Exercise 4: Redo exercise 3 with the "count" string method
print("In an even faster way, we found", testStr.count(userLetter), "instance(s) of your letter.\n")




# Exercise 5: Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence:0.8475'

# Use find and string slicing to extract the portion of the string after the colon character 
# and then use the float function to convert the extracted string into a floating point number.

newStr = float(str[str.find(':')+1:])
print(newStr)

# Exercise 6: Read the documentation of the string methods at https://docs.python.org/library/stdtypes.html#string-methods 
# You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful.

# The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), 
# the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.

