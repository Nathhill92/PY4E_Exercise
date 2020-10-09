# Create a function that counts the integer's number of digits.

# Examples
# count(318) ➞ 3
# count(-92563) ➞ 5
# count(4666) ➞ 4
# count(-314890) ➞ 6
# count(654321) ➞ 6
# count(638476) ➞ 6

# For an added challenge, try to solve this without using strings.

import random, math

def count_using_string(val):
    val = abs(val)
    return len(str(val))

#This method is MUCH faster for large numbers
#see - https://stackoverflow.com/questions/2189800/length-of-an-integer-in-python
def count_no_string(val):
    val = abs(val)
    return int(math.log10(val))+1

num = random.randrange(-1000000, 1000000)
print("Original Value:",num)
print("Number of digits:",count_using_string(num))
print("Number of digits without using string conversion:",count_no_string(num))