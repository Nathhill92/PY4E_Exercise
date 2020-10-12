#This code does not work for all test cases
#This was a little tough for my level - revisit with more experience
#For future attempts - Using two separate For loops to handle the logic is a bad design
#Go to one For loop and better track the "startpos"

# A group of n prisoners stand in a circle awaiting execution. Starting from an arbitrary position(0), the executioner kills every kth person until one person remains standing, who is then granted freedom (see examples).
# Create a function that takes 2 arguments — the number of people to be executed n, and the step size k, and returns the original position (index) of the person who survives.
# Examples
# who_goes_free(9, 2) ➞ 2
#  Prisoners = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#  Executed people replaced by - (a dash) for illustration purposes.
#  1st round of execution = [0, -, 2, -, 4, -, 6, -, 8]  -> [0, 2, 4, 6, 8]
#  2nd round = [-, 2, -, 6, -] -> [2, 6]  # 0 is killed in this round because it's beside 8 who was skipped over.
#  3rd round = [2, -]

# who_goes_free(9, 3) ➞ 0
#  [0, 1, 2, 3, 4, 5, 6, 7, 8]
#  [0, 1, -, 3, 4, -, 6, 7, -] -> [0, 1, 3, 4, 6, 7]
#  [0, 1, -, 4, 6, -] -> [0, 1, 4, 6]
#  [0, 1, -, 6] -> [0, 1, 6]
#  [0, -, 6] -> [0, 6]
#  [0, -] -> [0]

def who_goes_free(prisoners, step):
    #Create prisoner list
    startpos = step-1
    # plist = []
    # for x in range(prisoners):
    #     plist.append(str(x))
    
    #simplify with list comprehension
    plist = [str(x) for x in range(prisoners)]
    
    #loop for prisoner logic
    finished = False
    while not finished:
        print(plist)
        for x in range(startpos, len(plist), step):
            plist[x] = "-"
        
        #logic to handle "overflow" scenaries. When the kill order would not be starting from the beginning of the loop
        if plist[-1] != "-":
            try:
                pindex = ''.join(plist).rindex("-") - 1
                print(plist)
                for x in range(step-1-pindex, len(plist), step):
                    if x == len(plist)-1:
                        break
                    else:
                        plist[x] = "-"
                        if x + step > len(plist)-1:
                            startpos = step-1-x

            except:
                #This statement will get triggered in the event that there are no "-" values
                #i.e. "step" is larger than the legnth of prisoner list
                pindex = (step % len(plist)) - 1
                plist[pindex] = "-"

        #list string report and replace logic
        plist[:] = [x for x in plist if x != "-"]
        print(plist)
        
        #exit loop
        if len(plist) == 1:
            finished = True

    return plist

who_goes_free(9, 3)
#who_goes_free(41, 2)
#who_goes_free(14, 4)