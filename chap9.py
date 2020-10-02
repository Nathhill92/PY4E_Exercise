# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
# It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

# text = open("words.txt")

# wordsDict = {}

# for words in text:
#     words = words.split()
#     for word in words:
#         if word not in wordsDict:
#             wordsDict[word]=1
#         else:
#             wordsDict[word] += 1

# for x in wordsDict:
#     print(x, wordsDict[x])

# text.close()

# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. 
# To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. 
# At the end of the program print out the contents of your dictionary (order does not matter).

# mbox = open("mbox-short.txt")
# mboxDict = {}

# for messages in mbox:
#     message = messages.split()
#     if len(message) == 0 or message[0] != "From":
#         continue

#     if message[2] not in mboxDict:
#         mboxDict[message[2]] = 1
#     else:
#         mboxDict[message[2]] += 1

# for key in mboxDict:
#     print(key, mboxDict[key])

# Exercise 3: Write a program to read through a mail log, 
# build a histogram using a dictionary to count how many messages have come from each email address, 
# and print the dictionary.

mboxFrom = open("mbox-short.txt")
mboxFromDict = {}

for messages in mboxFrom:
    message = messages.split()
    if len(message) == 0 or message[0] != "From":
        continue

    if message[1] not in mboxFromDict:
        mboxFromDict[message[1]] = 1
    else:
        mboxFromDict[message[1]] += 1

print("Emails received by...")
for key in mboxFromDict:
    print(key, mboxFromDict[key])

# Exercise 4: Add code to the above program to figure out who has the most messages in the file.
#  After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop 
# (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

maxSender=None

for key in mboxFromDict:
    if maxSender is None or mboxFromDict[key] > mboxFromDict[maxSender]:
        maxSender = key

print("\nMost messages sent by...")
print(maxSender, mboxFromDict[maxSender])

mboxFrom.close()
print("\n")

# Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from 
# (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

mboxDomain = open("mbox-short.txt")
domainDict = {}

for messages in mboxDomain:
    message = messages.split()
    if len(message) == 0 or message[0] != "From":
        continue

    #strip email "from" and everything left of the "@"
    domain = message[1]
    domain = domain[domain.index("@"):]

    if domain not in domainDict:
        domainDict[domain] = 1
    else:
        domainDict[domain] += 1

for key in domainDict:
    print(key, domainDict[key])