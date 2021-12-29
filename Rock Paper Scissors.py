import random
import time

computer_wins = 0
player_wins = 0

def Choose_Option():
    user_choice = input("Please choose rock, paper or scissors: ")
    if user_choice in ["Rock", "rock", "r", "R", "ROCK"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P", "PAPER"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S","SCISSORS"]:
        user_choice = "s"
    else:
        print("\nTypeError. Please try again\n")
        Choose_Option()
    return user_choice

def Computer_Option():
    print("\nWaiting for a reply from the computer...\n")
    time.sleep(3)
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        computer_choice = "r"
    elif computer_choice == 2:
        computer_choice = "p"
    else:
        computer_choice = "s"
    return computer_choice


while True:
    print("")
   
    user_choice = Choose_Option()
    computer_choice = Computer_Option()

    print("")
   
    if user_choice == "r":
        if computer_choice == "r":
            print("Both outcomes were the same. It is a draw.")
       
        elif computer_choice == "p":
            print("The computer chose paper. You lose.")
            computer_wins += 1
           
        elif computer_choice == "s":
            print("The computer chose scissors. You win!")
            player_wins += 1

    elif user_choice == "p":
        if computer_choice == "r":
            print("The computer chose rock. You win!")
            player_wins += 1
       
        elif computer_choice == "p":
            print("Both outcomes were the same. It is a draw.")
           
           
        elif computer_choice == "s":
            print("The computer chose scissors. You lose.")
            computer_wins += 1

    elif user_choice == "s":
        if computer_choice == "r":
            print("The computer chose rock. You lose.")
            computer_wins += 1
       
        elif computer_choice == "p":
            print("The computer chose paper. You win!")
            player_wins += 1
           
        elif computer_choice == "s":
            print("Both outcomes were the same. It is a draw.")

    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(computer_wins))
    print("")
   
    user_choice = input("Do you want to play again? (Yes/No)")
    if user_choice in ["Y", "y", "yes", "Yes", "YES"]:
        pass
    elif user_choice in ["N", "n", "no", "No", "NO"]:
        break
    else:
        break
