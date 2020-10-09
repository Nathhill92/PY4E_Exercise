# A set is a collection of unique items. A set can be formed from a list from removing all duplicate items.

# [1, 3, 3, 5, 5, 5]
# # original list

# [1, 3, 5]
# # original list transformed into a set
# Create a function that sorts a list and removes all duplicate items from it.
import random

def setify(list):
    outlist = []
    for x in list:
        if x not in outlist:
            outlist.append(x)
    #
    #This does not work because the the ".sort()" function of the list object returns "None"
    #outlist would be equal to "None"
    #outlist = outlist.sort()
    #
    #use the function in place
    outlist.sort()

    return outlist

randomlist = []
for i in range(10):
    randomlist.append(random.randrange(1,10))

print("Original list:", randomlist, " -> Ordered set:", setify(randomlist))