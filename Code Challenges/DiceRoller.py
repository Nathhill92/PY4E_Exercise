import random

#usage
print("""Type 'q' or 'quit' to exit
Accepts inputs like:
1d6
2d4
1d20
3d12
""")


while True:
    #get input
    dice = input("Dice roll: ")

    #exit condition
    if dice.lower() == 'q' or dice.lower() == 'quit':
        exit()
    
    try:
        #process input string
        dindex = dice.index("d")
        rollcount = int(dice[:dindex])
        dicesize = int(dice[dindex+1:])

        #roll the dice
        rolltotal = 0
        print("Rolling...")
        for x in range(0, rollcount):
            roll = random.randrange(1, dicesize+1)
            print(roll)
            rolltotal += roll
        print("Total:", rolltotal)
    
    except:
        print("Make sure that data is formatted correctly.\nex. 5d10")
        continue