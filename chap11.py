import re

# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. 
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

userRegEx = input("Enter your regex expression: ")
mbox = open("words.txt")
counter=0

for line in mbox:
    line = line.rstrip()
    if re.search(userRegEx, line):
        counter += 1

print("words.txt had", counter, "lines that matched", userRegEx)

mbox.close()
print()

#Exercise 2: Write a program to look for lines of the form:

#"New Revision: 39772"
mbox = open("words.txt")

regex = "(New Revision:)+"
matchCount=0
matchTotal=0

for line in mbox:
    line = line.rstrip()
    if re.search(regex, line):
        line = line[line.index(":")+2:]
        line = float(line)
        matchTotal += line
        matchCount += 1
        print(line)

print("Match Count:", matchCount)
print("Match Total:", matchTotal)
