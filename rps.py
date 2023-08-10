"""
Rock Paper Scissors
Would you like to play a game of Rock, Paper, Scissors?
"""
from random import randrange


def rock_paper_scissors() -> None:
    """Takes user input, calculates a random rps throw,
    and prints whether the user won or lost."""
    rps_throw = randrange(1, 4)
    player_throw = player_input()
    throws = ["rock", "paper", "scissors"]
    outcome = f"Computer threw {throws[rps_throw-1]}. Player threw {throws[player_throw-1]}."

    if rps_throw == player_throw:
        print(f"{outcome} Player ties!")
    elif (rps_throw + 1) == player_throw or (rps_throw == 3 and player_throw == 1):
        print(f"{outcome} Player wins!")
    else:
        print(f"{outcome} Player loses!")


def player_input() -> int:
    """
    get player input 1, 2 or 3 for rps."""
    number = 0
    while number < 1 or number > 3:
        print("Please enter a number.")
        print("1 for rock")
        print("2 for paper.")
        print("3 for scissors.")
        number = input("Your number: ")
        try:
            number = int(number)
            if number < 1 or number > 3:
                raise ValueError()
            return number
        except ValueError:
            print(f"Number ({number}) input must be an integer 1, 2, or 3.")
            number = 0
    return None


if __name__ == "__main__":
    rock_paper_scissors()
