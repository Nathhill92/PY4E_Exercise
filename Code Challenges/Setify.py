# A set is a collection of unique items. A set can be formed from a list from removing all duplicate items.

# [1, 3, 3, 5, 5, 5]
# # original list

# [1, 3, 5]
# # original list transformed into a set
# Create a function that sorts a list and removes all duplicate items from it.
import random

def setify(list):
    # /
    #Revisited this one
    #There is a "set" data type in Python that will return a list of ordered, unique items
    return set(list)
    
    # outlist = []
    # for x in list:
    #     if x not in outlist:
    #         outlist.append(x)

    #outlist.sort()
    #return outlist

randomlist = []
for i in range(10):
    randomlist.append(random.randrange(1,10))

print("Original list:", randomlist, " -> Ordered set:", setify(randomlist))