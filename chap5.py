# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, 
# print out the total, count, and average of the numbers. 
# If the user enters anything other than a number, 
# detect their mistake using try and except and print an error message and skip to the next number.

#Exercise 2: Add logic for tracking minimum and maxmimum number

print("Usage: Enter a number. Number count, total, and average will be reported at the end.")
print("Type 'none' when you want to stop.")

#variables for loop
userNum=0
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

    #iterate count and total
    count += 1
    total = total + userNum

    #logic for min/max numbers
    if maxNum is None or userNum > maxNum:
        maxNum = userNum

    if minNum is None or userNum < minNum:
        minNum = userNum

#print stats
print("\nEnd stats:")
print("Count: ", count)
print("Total: ", total)
print("Average: ", total/count)
print("Minimum value entered: ", minNum)
print("Maximum value entered: ", maxNum, "\n")