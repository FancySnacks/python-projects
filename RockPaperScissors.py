import random
import sys

choices = ['ROCK', 'PAPER', 'SCISSORS']

player_score = 0
cpu_score = 0
points_to_win = 0
round_count = 0

#Ask player for their move and get random choice from computer in reponse
def chooseOption():
    global round_count
    round_count += 1
    print("\n------------")
    print("\nRound", round_count)
    while True:
        print("\nRock, paper or scissors?\n")
        player_choice = input("> ").upper()
        if player_choice.upper() in choices:
            #Computer picks random move
            cpu_choice = random.choice(choices)
            print(cpu_choice)
            getResult(player_choice, cpu_choice)
        #Show error if player types unexpected input
        else:
            print("Invalid input")
    return player_choice

#Compare player choices and determine who won the round
#Also determine if somebody reached the point limit
def getResult(player_choice, cpu_choice):
    global player_score
    global cpu_score
    if player_choice in "ROCK":
        if cpu_choice in "ROCK":
            print("It's a tie.")
        elif cpu_choice in "PAPER":
            print("You lose.")
            cpu_score += 1
        elif cpu_choice in "SCISSORS":
            print("You win.")
            player_score += 1
    if player_choice in "PAPER":
        if cpu_choice == "ROCK":
            print("You win.")
            player_score += 1
        elif cpu_choice in "PAPER":
            print("It's a tie.")
        elif cpu_choice in "SCISSORS":
            print("You lose.")
            cpu_score += 1
    if player_choice in "SCISSORS":
        if cpu_choice in "ROCK":
            print("You lose.")
            cpu_score += 1
        elif cpu_choice in "PAPER":
            print("You win.")
            player_score += 1
        elif cpu_choice in "SCISSORS":
            print("It's a tie.")
    print("\nPlayer -", player_score, "|", "CPU -", cpu_score)
    if int(player_score) != int(points_to_win) and int(cpu_score) == int(points_to_win):
        chooseOption()
    elif int(player_score) == int(points_to_win):
        print("You are the winner!")
        askContinue()
    elif int(cpu_score) == int(points_to_win):
        print("I win!")
        askContinue()

#Choose the amount of points required to win
def gameStart():
    global points_to_win
    while True:
        print("Up to how many points do you want to play to?")
        points_to_win = input("> ")
        if points_to_win.isdigit():
            break
        else:
            print("Invalid input")
            continue
    print("First one to get", points_to_win, "points wins.")
    chooseOption()

#Close the game
def gameEnd():
    sys.exit(0)

#Restart the game and reset variables
def gameRestart():
    global player_score
    global cpu_score
    global points_to_win
    global round_count
    player_score = 0
    cpu_score = 0
    points_to_win = 0
    round_count = 0
    gameStart()

#Ask the player if he wishes to play a rematch
def askContinue():
    while True:
        print("\nDo you want to play again? [Y/N]")
        user_decision = input("> ")
        if user_decision in ("y", "Y"):
            gameRestart()
        elif user_decision in ("n", "N"):
            gameEnd()
        else:
            print("Invalid input")
            continue
        

print("Welcome to rock paper scissors!")
gameStart()