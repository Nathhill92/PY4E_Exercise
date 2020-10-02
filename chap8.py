# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. 
# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

# def Chop(list):
#     del list[0]
#     del list[-1]
#     return None

# def Middle(list):
#     newList = []
#     for item in list:
#         newList.append(item)
#     return newList[1:-1]

# userList = ["1", "2", 3,5,6,75]
# print(Middle(userList))

# Chop(userList)

# print(userList)

# Exercise 4: Download a copy of the file www.py4e.com/code3/romeo.txt. 
# Write a program to open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split function. 
# For each word, check to see if the word is already in a list. 
# If the word is not in the list, add it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.

#initialize variables
wordList = []

#open file
romeo = open("romeo.txt")

#go line-by-line
for line in romeo:
    words=line.split()
    #go word-by-word
    for word in words:
        if word not in wordList:
            wordList.append(word)

#reverse and print list
wordList.sort()
print(wordList)

romeo.close()

# Exercise 5: Write a program to read through the mail box data and when you find line that starts with “From”, 
# you will split the line into words using the split function. We are interested in who sent the message, which is the second word on the From line.

# example line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

# You will parse the From line and print out the second word for each From line, 
# then you will also count the number of From (not From:) lines and print out a count at the end

#open file
mbox = open("mbox-short.txt")

#initialize variables
fromCount=0

for line in mbox:
    line = line.split()
    if len(line) == 0 or line[0] != "From":
        continue
    else:
        fromCount += 1
    print(line)

print("There were", fromCount, "lines in the file with From as the first word.")

# Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the 
# user enters “done”. Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the 
# maximum and minimum numbers after the loop completes.

print("\n\n\nUsage: Enter a number. Number count, total, and average will be reported at the end.")
print("Type 'none' when you want to stop.")

#variables for loop
userNum=0
userNumList=[]
done=False
maxNum=None
minNum=None
count=0
total=0


while done==False:
    try:
        #take user input
        userNum = input("Enter a number: ")
        
        #exit if input is "none"
        if userNum == "none":
            done==True
            break
        
        #convert input to float. Failure will trigger except block and continue loop
        userNum = float(userNum)
    except:
        print("Invalid input")
        continue

    #iterate count and total, add to list of user numbers
    count += 1
    total = total + userNum
    userNumList.append(userNum)

#print stats
print("\nEnd stats:")
print("Count: ", count)
print("Total: ", total)
print("Average: ", total/count)
print("Minimum value entered: ", min(userNumList))
print("Maximum value entered: ", max(userNumList), "\n")