import random
import time

play = input("Do you want to play rock paper scissors? (Y/N)")
play = play.capitalize()
compMove = random.randint(1, 3)


def move(outcome):  # This function takes the outcome and prints it
    global compMove
    print("I chose....")
    time.sleep(1)
    print(compMove)
    print("That means " + outcome)


def compChoice():  # This function converts the var compMove from a number to a letter
    global compMove
    if compMove == 1:
        compMove = "rock"
    elif compMove == 2:
        compMove = "paper"
    elif compMove == 3:
        compMove = "scissors"


def playAgain():  # This function gives the options of playing again or ending the game
    global play
    global compMove
    time.sleep(1)
    compMove = random.randint(1, 3)
    play = input("Do you want to play again? (Y/N)")
    play = play.capitalize()


while play == "Y":
    userMove = input("Rock, Paper or Scissors?")
    userMove = userMove.lower()
    compChoice()
    print(compMove)

    if userMove == compMove:
        move("we tie!")
        playAgain()
    elif (userMove == "rock" and compMove == "paper") or (userMove == "scissors" and compMove == "rock") or (userMove == "paper" and compMove == "scissors"):
        move("I win!")
        playAgain()
    elif (userMove == "rock" and compMove == "scissors") or (userMove == "scissors" and compMove == "paper") or (userMove == "paper" and compMove =="rock"):
        move("you win!")
        playAgain()
    else:
        print("You sure you entered a valid move?")

if play == "N":
    print("Have a nice day!")
