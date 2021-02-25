#Imports various systems that will be in use here
import random
import sys

#Setting up variables
rounds = 0
round_count = 0
player_score = 0
pc_score = 0

#Script asks player how many rounds he wants to play
def roundsetup():
    global rounds
    rounds = input("How many rounds do you wish to play?\n")
    select()

#This function asks the player for his move by taking numerical input
#1 = rock, 2 = paper, 3 = scissors
def select():
    selection = input("What's your choice? 1 = rock, 2 = paper, 3 = scissors\n")
    if selection == "1" or "2" or "3":
        pc_select(selection)
    else:
        # If player types in invalid input the function asks him to choose once again
        select()
#Get random value and compare it to the player's selection
def pc_select(select):
    pc_select = (random.randint(1,3))
    choose_winner(select, pc_select)
    return pc_select

#Compare PC and player's selection and find out who won
#Rock, paper, scissors are in ascending order, whorever has superior / greater number wins
def choose_winner(select, pc_select):
    if int(select) == int(pc_select):
        #If both PC and player made the same selection the round ends in a tie
        print("It's a tie!")
        round_end("tie")
    elif int(select) > int(pc_select):
        #Player wins
        print("Player wins!")
        round_end("player")
    elif int(pc_select) > int(select):
        #PC wins
        print("PC wins!")
        round_end("pc")
    else:
        #This one will never trigger generally
        print("Somebody won and somebody lost idk")

#Whoever won gets the point to their score
def round_end(winner):
    global rounds
    global round_count
    round_count += 1
    if winner == "player":
        #Increase player score
        global player_score
        player_score += 1
    elif winner == "pc":
        #Increase PC score
        global pc_score
        pc_score += 1
    else:
        #If it's a tie, nobody gains a point
        select()
    if int(round_count) < int(rounds):
        #If the game is not over yet, ask the player for his choice once again
        select()
    else:
        #Once game ends, print scores and ask player if he wants to play again
        print("\n[Player score] = " + str(player_score) + "\n[PC Score] = " + str(pc_score))
        print("Thanks for playing!")
        ask_rematch()

#Ask player if he wants to play again
def ask_rematch():
    print("Would you like to play again? [Y/N]")
    decision = input()
    if decision in ("y", "Y"):
        #Restart the game
        restart()
    elif decision in ("n", "N"):
        #If player doesn't want to play again, close the game
        end()
    else:
        ask_rematch()

def restart():
    #Set variables to default
    global rounds
    rounds = 0
    global round_count
    round_count = 0
    global player_score
    player_score = 0
    global pc_score
    pc_score = 0
    roundsetup()

#Close the game
def end():
    sys.exit(0)

print("=== Welcome to Rock, Paper, Scissors! ===")
roundsetup()
