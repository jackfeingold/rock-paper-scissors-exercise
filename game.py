


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#



# Beginning of code for Rock Paper Scissors Exercise for Jack Feingold OPIM 243

# Welcome message and setup section
import random

print("Welcome to the Rock, Paper, Scissors Game!\n")
print("-----------------\n")

# User input section
switch = False

while switch == False:
    user_selection = input("Please enter 'Rock', 'Paper', or 'Scissors'.\n")

    user_selection = user_selection.lower()

    # Input Validation section
    if user_selection == "rock" or user_selection == "paper" or user_selection == "scissors":
        switch = True
        print("You chose " + user_selection + ".\n")
        print("-----------------\n")
    else:
        print("Please enter 'rock', 'paper', or 'scissors' and make sure that it is correctly spelled.")

# Computer selection
selection_options = ['rock','paper','scissors']
computer_choice = random.choice(selection_options)

# outcome determination
# no winner is 0, user win is 1, computer win is 2
if user_selection == computer_choice:
    outcome = 0
elif user_selection == "rock" and computer_choice == "scissors":
    outcome = 1
elif user_selection == "rock" and computer_choice =="paper":
    outcome = 2
elif user_selection == "paper" and computer_choice == "scissors":
    outcome = 2
elif user_selection == "paper" and computer_choice == "rock":
    outcome = 1
elif user_selection == "scissors" and computer_choice == "rock":
    outcome = 2
elif user_selection == "scissors" and computer_choice == "paper":
    outcome = 1


# outcome output to interface
if outcome == 0:
    print("The computer chose " + user_selection + " too!  There is no winner.")
elif outcome == 1:
    if user_selection == "rock":
        print("The computer chose scissors! You win!")
    elif user_selection == "paper":
        print("The computer chose rock! You win!")
    elif user_selection == "scissors":
        print("The computer chose paper! You win!")
elif outcome == 2:
    if user_selection == "rock":
        print("The computer chose paper.  You lose.")
    elif user_selection == "paper":
        print("The computer chose scissors.  You lose.")
    elif user_selection == "scissors":
        print("The computer chose rock.  You lose.")

print("\n")
print("-----------------\n")

# goodbye message
print("Thank you for playing.  Please play again!\n")



