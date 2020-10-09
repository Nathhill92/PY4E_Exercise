# Simple OOP Calculator
# Create methods for the Calculator class that can do the following:

# Add two numbers.
# Subtract two numbers.
# Multiply two numbers.
# Divide two numbers.
# Examples
# calculator = Calculator()

# calculator.add(10, 5) ➞ 15
# calculator.subtract(10, 5) ➞ 5
# calculator.multiply(10, 5) ➞ 50
# calculator.divide(10, 5) ➞ 2
# Notes
# The methods should return the result of the calculation.
# Don't worry about needing to handle division by zero errors.
# See the Resources tab for some helpful tutorials on Python classes. - https://edabit.com/challenge/ta8GBizBNbRGo5iC6

class calculator:
    def add(x,y):
        return x+y
    def subtract(x,y):
        return x-y
    def multiply(x,y):
        return x*y
    def divide(x,y):
        return x/y

x=10
y=5
print("x =",x,"y =",y)
print()
print("x + y =",calculator.add(x,y))
print("x - y =",calculator.subtract(x,y))
print("x * y =",calculator.multiply(x,y))
print("x / y =",calculator.divide(x,y))
