"""
Rock Paper Scissors
Would you like to play a game of Rock, Paper, Scissors?
"""
from random import randint


def rock_paper_scissors() -> None:
    """Takes user input, calculates a random rps throw,
    and prints whether the user won or lost."""
    rps_throw = randint(0, 2)



if __name__ == "__main__":
    rock_paper_scissors()
