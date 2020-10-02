# Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. 
# Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. 
# Then sort the list in reverse order and print out the person who has the most commits.

mboxFrom = open("mbox-short.txt")
mboxFromDict = {}
#added for exercise 2
mboxTime = None
mboxTimeDict = {}

for messages in mboxFrom:
    message = messages.split()
    if len(message) == 0 or message[0] != "From":
        continue

    if message[1] not in mboxFromDict:
        mboxFromDict[message[1]] = 1
    else:
        mboxFromDict[message[1]] += 1


    #added logic for later hour counts
    mboxTime = message[5][:2]
    if mboxTime not in mboxTimeDict:
        mboxTimeDict[mboxTime] = 1
    else:
        mboxTimeDict[mboxTime] += 1


# print("Emails received by...")
# for key in mboxFromDict:
#     print(key, mboxFromDict[key])

#Dictionary -> Tuple
#Tuples can be sorted more easily
mboxList = mboxFromDict.items()
newList = list()

#Reverse order from (Key, Value) -> (Value, Key), so that we can sort by value
for key, value in mboxList:
    newList.append((value, key))

#Give us the largest value and report it
newList.sort(reverse=True)
print(newList[0])

print()
# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. 
# You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. 
# Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

newTimeList = list()
for key, value in mboxTimeDict.items():
    newTimeList.append((key, value))

newTimeList.sort()

for x, y in newTimeList:
    print(x, y)

mboxFrom.close()
print()
#Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. 
# Your program should convert all the input to lower case and only count the letters a-z. 
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. 
# Find text samples from several different languages and see how letter frequency varies between languages. 
# Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

text = open("words.txt")
letterDict = {}

#Full text -> Lines -> Letters within lines
for lines in text:
    for letter in lines.lower():
        #logic for updating letter table
        if letter.isalpha() == False:
            continue
        else:
            if letter not in letterDict:
                letterDict[letter] = 1
            else:
                letterDict[letter] += 1

letterList = list()
for key, value in letterDict.items():
    letterList.append(((value, key)))

letterList.sort(reverse=True)

for x, y in letterList:
    print(y, x)