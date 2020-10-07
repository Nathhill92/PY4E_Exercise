import random

#Initialize variables
tiecount=0
p1wincount=0
losscount=0

#Rules of the game
def game(p1input, p2input):
    if p1input == p2input:
        print("Tie!")
        global tiecount
        tiecount+=1
    elif (p1input == "rock" and p2input == "scissors") or (p1input == "paper" and p2input == "rock") or (p1input == "scissors" and p2input == "paper"):
        print("Player 1 wins!")
        global p1wincount
        p1wincount+=1
    else:
        print("Computer wins!")
        global losscount
        losscount+=1

print("type quit or exit to leave the program")

while True:
    #get user input
    p1input = input("Rock, Paper, Scissors: ")
    p1input = p1input.lower()
    #print("Debugging... Player input: ", p1input)
    if p1input == "quit" or p1input == "exit":
        break
        
    #get computer input
    p2input = random.choice(['rock', 'paper', 'scissors'])
    print("Computer picks", p2input)

    #play game
    game(p1input, p2input)

print("\n\nWin count:", p1wincount, "Loss count:", losscount, "Tie count:", tiecount, "\n\n")