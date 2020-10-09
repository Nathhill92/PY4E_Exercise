import random

def bubble(listtosort):
    #list length is 1 fewer than the max for two reasons
    #   1: Avoid "out of index" errors
    #   2: Bubble sort moves the largest value to the right most position on each pass  
    listlength = len(listtosort)-1
    sorted = False
    #missed this While in my original loop. This is possible with nested For loops, but this While seems easier.
    while not sorted:
        sorted = True
        for i in range(0, listlength):
            if listtosort[i] > listtosort [i+1]:
                sorted = False
                #lists are MUTABLE, meaning that they are changeable
                #also this type of assignment saves having to use a "temp" variable
                listtosort[i], listtosort[i+1] = listtosort[i+1], listtosort[i]
        #Because each iteration will move the largest value to the right most position...
        #We no longer need to compare against the right most positions at we iterate! Saves a little compute.
        listlength -= 1
    return listtosort

#initialize variables
listtosort = []
returnlist = []
#create random list of integers to sort
for x in range(8):
    listtosort.append(random.randrange(-10,10))
#output
print("Random list to sort:",listtosort)
print("Sorted list:",bubble(listtosort))