import random
import time
import sys

#List of all possible responses
list = ["Most definitely",
"The chances are high",
"I'm 99.99% sure, yes",
"I'd say so",
"Cannot predict now",
"Probably",
"Ask later",
"Could be the case",
"Don't count on it",
"It's uncertain",
"Proably not",
"Not likely"]

#Take user input, if he types a question, generate random answer after a short time
#Or if he wishes to quit, end session
def takeInput():
    print("\nEnter your question")
    print("Or type 'Exit' to close\n")
    userinput = input("\n> ")
    if str(userinput) in ("exit", "Exit"):
        end()
    else:
        print("\nThinking...")
        time.sleep(2)
        print(random.choice(list))
        time.sleep(1)

        anotherQuestion()

#Ask user if he wants to ask another question or end session
#If user agrees, repeat takeInput() function
def anotherQuestion():
    while True:
        print("\nWould you like to ask another question? (Y/N)\n")
        userinput = input("\n> ")
        if str(userinput) in ("exit", "Exit", "No", "no", "N", "n"):
            end()
        elif str(userinput) in ("Yes", "yes", "Y", "y"):
            takeInput()
        else:
            continue
        
#End the session
def end():
    print("\nThanks for playing!")
    sys.exit(0)

#Welcome message and function call that appears at the launch
print("Welcome to the Magic 8 Ball!")
takeInput()