import random

#get/validate input
def UserInput():
    usernum = input("Choose a number between 1 and 100: ")

    #validate input
    try:
        usernum = int(usernum)
        if usernum > 100 or usernum < 1:
            print("Please enter a number in the correct range")
            return "continue"
    except:
        print("Uh oh! Make sure you entered a integer value between 1 and 100.")
        return "continue"

    return usernum

def GameLogic(usernum, answer, score):
    if usernum == answer:
        EndGame("win", answer, score)
    else:
        HintLogic(usernum, answer, score)

def HintLogic(usernum, answer, score):
    
    if score <= 4:
        if usernum > answer:
            print("The answer is SMALLER than your guess")
        else:
            print("The answer is LARGER than your guess")
    
    if score <= 3:
        if answer%2 == 0:
            print("The answer is an even number")
        else:
            print("The answer is an odd number")
   
    if score <= 2:
        outStr = "The answer is divisible by the following numbers... "
        for x in range(3,51):
            if answer%x == 0:
                outStr += "\n" + str(x)
        print(outStr)
    
    if score <= 1:
        EndGame("lose", answer, 0)

#Idea for future programs
#Plaintext on leaderboard
#Write lifetime total and highest single game total based on username
def EndGame(result, answer, score):
    if result == "win":
        print("Congrats! You guessed the right number with", score, "point(s)!")
        exit()
    else:
        print("Darn. Out of guesses. The answer was", answer)
        print("Better luck next time!")
        exit()


#Rules
print("""
Welcome to the Number Guessing game!

Rules are as follows:
You get 3 guesses to find a number between 1 and 100.
You will get clues along the way.
Guessing correctly with fewer clues will result in a higher score.
Good luck!

""")
#Generate random number
answer = random.choice(range(1, 101))
#initiazlize score
score=4

while score > 0:
    #print("\n\nDebugging... Answer", answer, "Score", score, "\n\n")
    #get/validate input
    usernum = UserInput()
    if usernum == "continue":
        continue

    #game logic
    GameLogic(usernum, answer, score)

    #decrement score
    score -= 1