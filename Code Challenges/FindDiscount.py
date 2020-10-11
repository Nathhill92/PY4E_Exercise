# Create a function that takes two arguments: the final price and the discount as integers and returns the final price after the discount.
# Examples
# dis(1500, 50) ➞ 750
# dis(89, 20) ➞ 71.2
# dis(100, 75) ➞ 25
# This one is a little *too* easy. Let's add processing for unique inputs

import re

def dis(price,discount):
    #handle price value inputs that are not integers/float:
    if not str(price).isnumeric():
        #use regex to remove non-numeric values - \d = all digits
        price = re.sub(r'[^\d\-.]', '', price)
        price = float(price)
    #handle discount value inputs that are not integers/float:
    if not str(discount).isnumeric():
        discount = re.sub(r'[^\d\-.]', '', discount)
        discount = float(discount)
    if discount > 1:
        discount = discount/100


    newprice = price * (1-discount)
    newprice = "${:,.2f}".format(newprice)
    return newprice

print(dis(1500,50))
print(dis("$952.25", 12))
print(dis("$7,182.50","26.55%"))
print(dis("$10,000.50",".25%"))
