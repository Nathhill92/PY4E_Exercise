# Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:

# python shout.py
# Enter a file name: mbox-short.txt
# FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
# RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
# RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#      BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#      SAT, 05 JAN 2008 09:14:16 -0500
# You can download the file from www.py4e.com/code3/mbox-short.txt
import os

inboxFile = open("mbox-short.txt")

# for line in inboxFile:
#     print(line.upper())

# Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:

# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the 
# floating-point number on the line. Count these lines and then compute the total of the spam confidence 
# values from these lines. When you reach the end of the file, print out the average spam confidence.

# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745

# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519
# Test your file on the mbox.txt and mbox-short.txt files.

spamCountTotal=0
spamConfidenceTotal=0

for line in inboxFile:
    if "X-DSPAM-Confidence:" in line:
        spamConf = float(line[line.find(":")+1:])
        
        spamCountTotal += 1
        spamConfidenceTotal += spamConf

print("The average spam confidence is: ", spamConfidenceTotal/spamCountTotal)