# A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.
# Create a function that determines whether a number is a Disarium or not.

# Examples
# is_disarium(75) ➞ false
# 7^1 + 5^2 = 7 + 25 = 32

# is_disarium(135) ➞ true
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

# is_disarium(518) ➞ true
# is_disarium(8) ➞ true

def is_disarium(num):
    print("Testing number:",num)
    total = 0
    #Read about the enumerate function, which made this section much more simple to write
    for x,y in enumerate(str(num)):
        total += int(y)**(x+1)
    print("Disarium total:",total)
    print((total == num))


is_disarium(75)
is_disarium(135)
is_disarium(14)
is_disarium(210)
is_disarium(518)
is_disarium(8)