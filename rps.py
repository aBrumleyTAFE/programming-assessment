import random


# defined function entitled game
def game():

    print("Hello, let's play Rock, Paper, Scissors!")

    # the user enters their name
    while True:
        userName = input("Enter your name and press Enter: ").lower().rstrip()
        if userName != "":
            break
    print("Hello", userName)

    # game loop
    while True:
        # resets the score to 0 each time a new match is played
        userScore = 0
        computerScore = 0

        # round loop - the following code executes as long as the score is less than 5
        while userScore < 5 and computerScore < 5:
            # choice options
            optionList = ("rock", "paper", "scissors")

            # user's choice
            while True:
                userInput = (
                    input("Type your choice here (rock or paper or scissors): ")
                    .lower()
                    .rstrip()
                )
                if userInput in optionList:
                    break
            # this prints out the user's choice
            print("You chose:\t\t" + userInput)

            # this variable will store the computer's choice and randomises the above option list
            computerChoice = random.choice(optionList)
            # this prints out the computer's choice
            print("Computer chose:\t\t" + computerChoice)

            rock = "rock"
            paper = "paper"
            scissors = "scissors"
            # checking winner
            if userInput == computerChoice:
                print(
                    "That's a draw! The score is: Computer: ",
                    computerScore,
                    " ",
                    userName,
                    " : ",
                    userScore,
                )
            elif userInput == rock and computerChoice == scissors:
                userScore = userScore + 1
                print(
                    "You win! The score is: Computer: ",
                    computerScore,
                    " ",
                    userName,
                    " : ",
                    userScore,
                )
            elif userInput == rock and computerChoice == paper:
                computerScore = computerScore + 1
                print(
                    "Computer wins! The score is: Computer: ",
                    computerScore,
                    " ",
                    userName,
                    " : ",
                    userScore,
                )
            elif userInput == paper and computerChoice == rock:
                userScore = userScore + 1
                print(
                    "You win! The score is: Computer: ",
                    computerScore,
                    " ",
                    userName,
                    " : ",
                    userScore,
                )
            elif userInput == paper and computerChoice == scissors:
                computerScore = computerScore + 1
                print(
                    "Computer wins! The score is: Computer: ",
                    computerScore,
                    " ",
                    userName,
                    " : ",
                    userScore,
                )
            elif userInput == scissors and computerChoice == paper:
                userScore = userScore + 1
                print(
                    "You win! The score is: Computer: ",
                    computerScore,
                    " ",
                    userName,
                    " : ",
                    userScore,
                )
            elif userInput == scissors and computerChoice == rock:
                computerScore = computerScore + 1
                print(
                    "Computer wins! The score is: Computer: ",
                    computerScore,
                    " ",
                    userName,
                    " : ",
                    userScore,
                )

        # message to winning user once score reaches 5
        if userScore == 5:
                print(f"Congratulations {userName}! You have won the match!")
        elif computerScore == 5:
            print(f"Sorry {userName}, the computer has won the match!")

        # if the user doesn't choose 'Yes', the process doesn't reset
        newGame = (
            input("Do you want to play again?: ").lower().rstrip()
        )
        if newGame != "yes" and newGame != "y":
            print("Thanks for playing!")
            break


game()  # game function called again if user inputs 'Yes'
