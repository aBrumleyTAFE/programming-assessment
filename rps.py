import random
#import something we can use for scoreboard

# queries player name
def q_name():
    # intro message
    # ask for name
        # input validation - strip spaces, do not allow empty input
    # greet player
    # return name

# queries for how many rounds
def q_rounds():
    # asks for rounds
        # input validation - repeat until selection is an odd number less then 10
    # returns choice
        ### CHANGE TO LOOP GOING THROUGH THIS

# game loop
def g_loop(game_rounds):
    # game loop should be moved here
    # for rounds in game_rounds
        # g_round
        # g_check
        # check if winner
            # break if winner and return computer or player name

# game round
def g_round():
    # player choice
        # input validation - set to lower, strip spaces, suggest r/p/s and check for r/p/s/rock/paper/scissor
    # comp choice from random
    # return choices - probably easiest to do as two variables ie `return playerChoice, cpuChoice`
        # we could also use a named tuple or list if we need it

# comparing choices to define winner
def g_check(pChoice, cChoice):
    # move the big if statement here

# taking things and putting them in the scoreboard
def s_write():
    # load scoreboard file
    # write winner, total rounds, and rounds won

# scoreboard
def s_board():
    # if program is run with `-s` or `--scoreboard`
    # load from scoreboard file
    # print it

def game():  # defined function entitled game

    print("Hello, let's play Rock, Paper, Scissors!")

    userName = input("Enter your name and press Enter: ")  # the user enters their name

    print("Hello ", userName)

    while True:  # this resets the score to 0 each time a new match is played

        userScore = 0
        computerScore = 0

        while (
            userScore < 5 and computerScore < 5
        ):  # the following code executes as long as the score is less than 5

            userInput = input(
                "Type your choice here (rock or paper or scissors) and press Enter: "
            )  # this variable will store the user's choice

            print("You chose " + userInput)  # this prints out the user's choice

            optionList = ("rock", "paper", "scissors")

            computerChoice = random.choice(
                optionList
            )  # this variable will store the computer's choice and randomises the above option list

            print(
                "Computer chose: " + computerChoice
            )  # this prints out the computer's choice

            a = "rock"

            b = "paper"

            c = "scissors"

            if (
                userInput == a and computerChoice == a
            ):  # if user and computer both choose rock
                print(
                    "That's a draw! The score is: Computer: ",
                    computerScore,
                    " ",
                    userName,
                    " : ",
                    userScore,
                )

            elif (
                userInput == b and computerChoice == b
            ):  # if user and computer both choose paper
                print(
                    "That's a draw! The score is: Computer: ",
                    computerScore,
                    " ",
                    userName,
                    " : ",
                    userScore,
                )

            elif (
                userInput == c and computerChoice == c
            ):  # if user and computer both choose scissors
                print(
                    "That's a draw! The score is: Computer: ",
                    computerScore,
                    " ",
                    userName,
                    " : ",
                    userScore,
                )

            elif (
                userInput == a and computerChoice == b
            ):  # if user enters rock and computer enters paper
                computerScore = (
                    computerScore + 1
                )  # score is updated with computer's win
                print(
                    "Computer wins! The score is: Computer: ",
                    computerScore,
                    " ",
                    userName,
                    " : ",
                    userScore,
                )
                if (
                    computerScore == 5 or userScore == 5
                ):  # score is out of 5, so once this is reached, the game is over
                    print("Game over!")
                    break

            elif (
                userInput == b and computerChoice == a
            ):  # if user enters paper and computer enters rock
                userScore = userScore + 1  # score is updated with user's win
                print(
                    "You win! The score is: Computer: ",
                    computerScore,
                    " ",
                    userName,
                    " : ",
                    userScore,
                )
                if computerScore == 5 or userScore == 5:
                    print("Game over!")
                    break

            elif (
                userInput == b and computerChoice == c
            ):  # if user enters paper and computer enters scissors
                computerScore = (
                    computerScore + 1
                )  # score is updated with computer's win
                print(
                    "Computer wins! The score is: Computer: ",
                    computerScore,
                    " ",
                    userName,
                    " : ",
                    userScore,
                )
                if computerScore == 5 or userScore == 5:
                    print("Game over!")
                    break

            elif (
                userInput == c and computerChoice == b
            ):  # if user enters scissors and computer enters paper
                userScore = userScore + 1  # score is updated with user's win
                print(
                    "You win! The score is: Computer: ",
                    computerScore,
                    " ",
                    userName,
                    " : ",
                    userScore,
                )
                if computerScore == 5 or userScore == 5:
                    print("Game over!")
                    break

            elif (
                userInput == c and computerChoice == a
            ):  # if user enters scissors and computer enters rock
                computerScore = (
                    computerScore + 1
                )  # score is updated with computer's win
                print(
                    "Computer wins! The score is: Computer: ",
                    computerScore,
                    " ",
                    userName,
                    " : ",
                    userScore,
                )
                if computerScore == 5 or userScore == 5:
                    print("Game over!")
                    break

            elif (
                userInput == a and computerChoice == c
            ):  # if user enters rock and computer enters scissors
                userScore = userScore + 1  # score is updated with user's win
                print(
                    "You win! The score is: Computer: ",
                    computerScore,
                    " ",
                    userName,
                    " : ",
                    userScore,
                )
                if computerScore == 5 or userScore == 5:
                    print("Game over!")
                    break

            else:
                print(
                    "You did not enter an option correctly"
                )  # message to the user if option hasn't been entered correctly

        if (
            userScore == 5 or computerScore == 5
        ):  # message to winning user once score reaches 5
            if userScore == 5:
                print(f"Congratulations {userName}! You have won the match!")
        else:
            print(f"Sorry {userName}, the computer has won the match!")

        newGame = input(f"Do you want to play again? Type 'Yes' or 'No': ")

        if (
            newGame != "Yes"
        ):  # if the user doesn't choose 'Yes', the process doesn't reset

            print("Thanks for playing!")
            break


game()  # game function called again if user inputs 'Yes'
