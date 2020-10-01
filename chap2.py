#Chapter 2 exercises
#https://www.py4e.com/html3/02-variables

#Write a program that uses input to prompt the user for their name and then welcomes them
# name = input("Hello! What is your name? ")
# print("Hello " +name)

# print()

#Write a program to prompt users for hours and hourly rate to compute gross wage
hours = input("Enter hours: ")
rate = input("Hourly rate: ")
pay = float(hours) * float(rate)
print("Pay $" + str(round(pay, 2)))

#Exercise 4: Assume that we execute the following assignment statements:
# width = 17
# height = 12.0
# For each of the following expressions, write the value of the expression and the type (of the value of the expression).

# width//2
# width/2.0
# height/3
# 1 + 2 * 5

width = 17
height = 12.0

print(width//2)
print(type(width//2))

print(width/2.0)
print(type(width/2.0))

print(height/3)
print(type(height/3))

print(1+2*5)
print(type(1+2*5))
print()
#Exercise 5: Write a program which prompts the user for a Celsius temperature, 
# convert the temperature to Fahrenheit, and print out the converted temperature.

tempInCel = float(input("Temp in C: "))
tempInFar = tempInCel * (9/5) + 32
print("Temp in F: " +str(tempInFar))