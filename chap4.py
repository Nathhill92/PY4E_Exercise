#chapter 4 assignments
import random

#assignment #1: Run random commands multiple times and compare output

for i in range(10):
    print(random.randint(1, 10000))

for i in range(10):
    print(random.choice(range(1, 50)))

#assignment #2: Functions basics

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

#Exercise 6: Rewrite payment as a function
#take/validate input
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

def Pay(hours, rate):
    if hours <= 40:
        pay = hours*rate
    else:
        pay = 40*rate
        overtimePay = (hours-40) * (rate*1.5)
        pay = pay + overtimePay
    return "Pay $" + str(round(pay, 2))

print(Pay(hours, rate))

#exercise 7: rewrite grade program as a function

#logic for user scores
def Grade(score):
    if score > 1 or score < 0:
        return("Bad Score. Please use a number in the 0.0 - 1.0 range")
    elif score >= .9:
        print("A")
    elif score >= .8:
        print("B")
    elif score >= .7:
        print("C")
    elif score >= .6:
        print("D")
    elif score > 0 and score < .6:
        print("F")
    else:
        print("Something went wrong")

#get and validate user input
score = input("Enter a score (0.0 - 1.0): ")
try:
    score=float(score)
except:
    print("Bad Score. Please use a number in the 0.0 - 1.0 range")
    exit()

#run it!
Grade(score)
