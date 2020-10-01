#Chapter 3 assignments


#Exercise 1 and 2: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

#user input
try:
    hours = float(input("Enter hours: "))
except:
    print("Please enter a numeric value")
    exit()

try:
    rate = float(input("Hourly rate: "))
except:
    print("Please enter a numeric value")
    exit()

#calculate pay
if hours <= 40:
    pay = hours*rate
else:
    pay = 40*rate
    overtimePay = (hours-40) * (rate*1.5)
    pay = pay + overtimePay

#print pay
print("Pay $" + str(round(pay, 2)))

#Exercise 3: prompt for a number between 0. - 1.0, print a grade based on the number

#get and validate user input
userNum = input("Enter a score (0.0 - 1.0): ")
try:
    userNum=float(userNum)
except:
    
    print("Bad Score. Please use a number in the 0.0 - 1.0 range")
    exit()

#logic for user scores
if userNum > 1 or userNum < 0:
    print("Bad Score. Please use a number in the 0.0 - 1.0 range")
    exit()
elif userNum >= .9:
    print("A")
elif userNum >= .8:
    print("B")
elif userNum >= .7:
    print("C")
elif userNum >= .6:
    print("D")
elif userNum > 0 and userNum < .6:
    print("F")
else:
    print("Something went wrong")
    exit()

    
